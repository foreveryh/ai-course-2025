#!/usr/bin/env python3
"""
Display a comprehensive summary of the parsed slide deck.
Shows key statistics and details about each slide's structure.
"""

import json
from pathlib import Path

def load_parsed_slides(json_path: str):
    """Load the parsed slides from JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_slides(slides):
    """Analyze the parsed slides and generate summary statistics."""
    
    # Basic statistics
    total_slides = len(slides)
    slides_with_front_matter = sum(1 for s in slides if s['has_front_matter'])
    slides_with_titles = sum(1 for s in slides if s['title'])
    
    # Front-matter analysis
    front_matter_keys = {}
    for slide in slides:
        if slide['front_matter']:
            for key in slide['front_matter'].keys():
                front_matter_keys[key] = front_matter_keys.get(key, 0) + 1
    
    # Content length analysis
    content_lengths = [len(slide['content']) for slide in slides]
    avg_content_length = sum(content_lengths) / len(content_lengths) if content_lengths else 0
    max_content_length = max(content_lengths) if content_lengths else 0
    min_content_length = min(content_lengths) if content_lengths else 0
    
    # Layout types
    layout_types = {}
    for slide in slides:
        if slide['front_matter'] and 'layout' in slide['front_matter']:
            layout = slide['front_matter']['layout']
            layout_types[layout] = layout_types.get(layout, 0) + 1
    
    return {
        'total_slides': total_slides,
        'slides_with_front_matter': slides_with_front_matter,
        'slides_with_titles': slides_with_titles,
        'front_matter_keys': front_matter_keys,
        'content_stats': {
            'avg_length': avg_content_length,
            'max_length': max_content_length,
            'min_length': min_content_length
        },
        'layout_types': layout_types
    }

def print_summary(slides):
    """Print a detailed summary of the parsed slides."""
    
    stats = analyze_slides(slides)
    
    print("=" * 70)
    print("SLIDE DECK ANALYSIS SUMMARY")
    print("=" * 70)
    
    print(f"\n📊 BASIC STATISTICS:")
    print(f"  • Total slides: {stats['total_slides']}")
    print(f"  • Slides with front-matter: {stats['slides_with_front_matter']} ({stats['slides_with_front_matter']/stats['total_slides']*100:.1f}%)")
    print(f"  • Slides with titles: {stats['slides_with_titles']} ({stats['slides_with_titles']/stats['total_slides']*100:.1f}%)")
    
    print(f"\n📐 CONTENT LENGTH STATISTICS:")
    print(f"  • Average content length: {stats['content_stats']['avg_length']:.0f} chars")
    print(f"  • Maximum content length: {stats['content_stats']['max_length']} chars")
    print(f"  • Minimum content length: {stats['content_stats']['min_length']} chars")
    
    if stats['front_matter_keys']:
        print(f"\n🔑 FRONT-MATTER KEYS USAGE:")
        for key, count in sorted(stats['front_matter_keys'].items(), key=lambda x: -x[1]):
            print(f"  • {key}: used in {count} slides")
    
    if stats['layout_types']:
        print(f"\n📑 LAYOUT TYPES:")
        for layout, count in sorted(stats['layout_types'].items(), key=lambda x: -x[1]):
            print(f"  • {layout}: {count} slides")
    
    print(f"\n📝 SLIDE DETAILS:")
    print("-" * 70)
    
    for slide in slides:
        # Print slide header
        title = slide['title'] if slide['title'] else "(No title)"
        print(f"\nSlide {slide['index']:2d}: {title}")
        
        # Print front-matter info
        if slide['has_front_matter']:
            fm_keys = list(slide['front_matter'].keys())
            print(f"  Front-matter: {', '.join(fm_keys)}")
            
            # Show specific front-matter values for key properties
            if 'layout' in slide['front_matter']:
                print(f"    - layout: {slide['front_matter']['layout']}")
            if 'image' in slide['front_matter']:
                print(f"    - image: {slide['front_matter']['image']}")
            if 'url' in slide['front_matter']:
                print(f"    - url: {slide['front_matter']['url']}")
        else:
            print(f"  Front-matter: None")
        
        # Content preview
        content_preview = slide['content'][:100].replace('\n', ' ')
        if len(slide['content']) > 100:
            content_preview += "..."
        print(f"  Content: {content_preview}")
        print(f"  Length: {len(slide['content'])} chars")
    
    print("\n" + "=" * 70)
    print("PARSING COMPLETE - All slides stored with index, raw markdown, and front-matter")
    print("=" * 70)

def main():
    """Main function to display slide summary."""
    
    # Load parsed slides
    json_path = 'parsed_slides.json'
    
    if not Path(json_path).exists():
        print(f"Error: {json_path} not found. Please run parse_slides.py first.")
        return
    
    slides = load_parsed_slides(json_path)
    
    # Print comprehensive summary
    print_summary(slides)
    
    print(f"\n✅ Successfully parsed and stored {len(slides)} slide objects")
    print("   Each slide contains:")
    print("   • index: sequential slide number")
    print("   • raw_markdown: original markdown content")  
    print("   • front_matter: parsed YAML metadata (if present)")
    print("   • content: slide content without front-matter")
    print("   • has_front_matter: boolean flag")
    print("   • title: extracted title (if present)")

if __name__ == "__main__":
    main()
