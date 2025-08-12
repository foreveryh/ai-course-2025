#!/usr/bin/env python3
"""
Parse slide deck markdown file into structured slide objects.
Splits content by '---' delimiter and extracts front-matter and content for each slide.
"""

import re
import yaml
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

class SlideParser:
    """Parser for markdown slide deck with front-matter support."""
    
    def __init__(self, file_path: str):
        """Initialize parser with file path."""
        self.file_path = Path(file_path)
        self.raw_content = ""
        self.slides = []
        
    def read_file(self) -> str:
        """Read the markdown file content."""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.raw_content = f.read()
        return self.raw_content
        
    def parse_front_matter(self, content: str) -> tuple[Optional[Dict[str, Any]], str]:
        """
        Extract YAML front-matter from content if present.
        Returns (front_matter_dict, remaining_content)
        """
        # Check if content starts with front-matter
        if content.strip().startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                # First part is empty, second is front-matter, third is content
                try:
                    front_matter = yaml.safe_load(parts[1])
                    remaining_content = parts[2].strip()
                except yaml.YAMLError:
                    # If YAML parsing fails, treat as regular content
                    return None, content.strip()
                return front_matter, remaining_content
        return None, content.strip()
        
    def parse_slides(self) -> List[Dict[str, Any]]:
        """
        Parse the markdown content into slide objects.
        Each slide contains:
        - index: slide number (1-based)
        - raw_markdown: original markdown content
        - front_matter: parsed front-matter (if present)
        - content: slide content without front-matter
        """
        if not self.raw_content:
            self.read_file()
            
        # Split content by '---' separators
        # Note: In Slidev, front-matter can appear after a '---' separator
        parts = self.raw_content.split('---')
        
        slide_parts = []
        i = 0
        while i < len(parts):
            part = parts[i].strip()
            
            # Skip empty parts
            if not part:
                i += 1
                continue
                
            # Check if this part looks like front-matter (key: value format)
            if ':' in part and not part.startswith('#'):
                # This might be front-matter
                # Check if there's content after it
                if i + 1 < len(parts):
                    next_part = parts[i + 1].strip()
                    # Combine front-matter with the following content
                    combined = f"---\n{part}\n---\n{next_part}"
                    slide_parts.append(combined)
                    i += 2  # Skip the next part as we've already processed it
                else:
                    # Front-matter at the end (unusual but handle it)
                    slide_parts.append(f"---\n{part}\n---")
                    i += 1
            else:
                # Regular content slide
                slide_parts.append(part)
                i += 1
        
        # Parse each slide
        self.slides = []
        slide_index = 0
        for slide_raw in slide_parts:
            if not slide_raw.strip():
                continue
            
            slide_index += 1
            # Parse front-matter if present
            front_matter, content = self.parse_front_matter(slide_raw.strip())
            
            slide_obj = {
                'index': slide_index,
                'raw_markdown': slide_raw.strip(),
                'front_matter': front_matter,
                'content': content,
                'has_front_matter': front_matter is not None
            }
            
            # Extract title if present (first # heading)
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if title_match:
                slide_obj['title'] = title_match.group(1).strip()
            else:
                slide_obj['title'] = None
                
            self.slides.append(slide_obj)
            
        return self.slides
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the parsed slides."""
        if not self.slides:
            self.parse_slides()
            
        return {
            'total_slides': len(self.slides),
            'slides_with_front_matter': sum(1 for s in self.slides if s['has_front_matter']),
            'slides_with_titles': sum(1 for s in self.slides if s.get('title')),
            'front_matter_keys': self._get_all_front_matter_keys(),
            'slide_titles': [s.get('title', f"Slide {s['index']} (no title)") for s in self.slides]
        }
    
    def _get_all_front_matter_keys(self) -> List[str]:
        """Get all unique front-matter keys used across slides."""
        keys = set()
        for slide in self.slides:
            if slide['front_matter']:
                keys.update(slide['front_matter'].keys())
        return sorted(list(keys))
    
    def save_to_json(self, output_path: str):
        """Save parsed slides to JSON file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.slides, f, ensure_ascii=False, indent=2)
            
    def print_slide_info(self, slide_index: int):
        """Print detailed info for a specific slide."""
        if not self.slides:
            self.parse_slides()
            
        for slide in self.slides:
            if slide['index'] == slide_index:
                print(f"\n{'='*50}")
                print(f"SLIDE {slide['index']}")
                print(f"{'='*50}")
                
                if slide['has_front_matter']:
                    print("\nFront-matter:")
                    print(yaml.dump(slide['front_matter'], allow_unicode=True))
                else:
                    print("\nNo front-matter")
                    
                print("\nContent preview (first 200 chars):")
                print(slide['content'][:200] + "..." if len(slide['content']) > 200 else slide['content'])
                
                if slide.get('title'):
                    print(f"\nTitle: {slide['title']}")
                    
                print(f"\nRaw markdown length: {len(slide['raw_markdown'])} chars")
                return
                
        print(f"Slide {slide_index} not found")


def main():
    """Main function to parse the slide deck."""
    # Parse the slide deck
    parser = SlideParser('pages/01-intro.md')
    
    # Read and parse the file
    parser.read_file()
    slides = parser.parse_slides()
    
    # Print summary
    print("SLIDE DECK PARSING COMPLETE")
    print("="*50)
    
    summary = parser.get_summary()
    print(f"\nTotal slides: {summary['total_slides']}")
    print(f"Slides with front-matter: {summary['slides_with_front_matter']}")
    print(f"Slides with titles: {summary['slides_with_titles']}")
    
    print(f"\nFront-matter keys found: {', '.join(summary['front_matter_keys']) if summary['front_matter_keys'] else 'None'}")
    
    print("\n\nSlide Overview:")
    print("-"*50)
    for i, title in enumerate(summary['slide_titles'], 1):
        print(f"  {i:2d}. {title}")
    
    # Save to JSON for later analysis
    parser.save_to_json('parsed_slides.json')
    print(f"\n\nParsed slides saved to: parsed_slides.json")
    
    # Show details of first few slides as examples
    print("\n\nDETAILED VIEW OF FIRST 3 SLIDES:")
    for i in range(1, min(4, len(slides) + 1)):
        parser.print_slide_info(i)


if __name__ == "__main__":
    main()
