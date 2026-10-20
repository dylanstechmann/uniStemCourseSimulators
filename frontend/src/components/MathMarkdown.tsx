import "katex/dist/katex.min.css";
import Markdown from "react-markdown";
import rehypeKatex from "rehype-katex";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import { markdownComponents } from "./MarkdownReader";

/** Markdown with KaTeX math, loaded as a separate chunk only for text that contains math. */
export default function MathMarkdown({ children }: { children: string }) {
  return (
    <Markdown
      skipHtml
      remarkPlugins={[remarkGfm, remarkMath]}
      rehypePlugins={[[rehypeKatex, { strict: "ignore" }]]}
      components={markdownComponents}
    >
      {children}
    </Markdown>
  );
}
