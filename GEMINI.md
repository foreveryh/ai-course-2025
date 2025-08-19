# GEMINI.md

## Project Overview

This project is a comprehensive AI course created with [Slidev](https://sli.dev), a presentation framework for developers. The course is designed for individual entrepreneurs, independent developers, and product managers. It covers the fundamentals of Large Language Models (LLMs), their capabilities and limitations, prompt engineering, and practical applications using tools like Google AI Studio.

The project is structured as a series of Markdown files that are compiled into a web-based presentation. It includes slides, code examples, and practical exercises.

**Key Technologies:**

*   **Framework:** Slidev
*   **Language:** Vue 3 + TypeScript + Markdown
*   **Styling:** UnoCSS + TailwindCSS
*   **Deployment:** Vercel

## Building and Running

### Prerequisites

*   Node.js >= 18
*   npm or pnpm

### Development

To start the local development server:

```bash
npm run dev
```

This will open the presentation in your browser at `http://localhost:3030`.

### Build

To build the static files for production:

```bash
npm run build
```

The output will be in the `dist` directory.

### PDF Export

To export the presentation as a PDF:

```bash
npm run export
```

Note: This requires `playwright-chromium` to be installed.

## Development Conventions

*   **Content Organization:** The course content is modularized into separate `.md` files in the `pages` directory. The main entry point is `slides.md`.
*   **Static Assets:** All static assets like images and videos are stored in the `public` directory.
*   **Custom Components:** The project uses custom Vue components located in the `components` directory to enhance the presentation with interactive elements.
*   **Styling:** The project uses UnoCSS and TailwindCSS for styling.
*   **Deployment:** The project is configured for deployment on Vercel. The configuration is in `vercel.json`.
