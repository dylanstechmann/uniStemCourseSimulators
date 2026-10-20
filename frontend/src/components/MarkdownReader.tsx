import { lazy, Suspense } from "react";
import Markdown, { type Components } from "react-markdown";
import remarkGfm from "remark-gfm";

const MathMarkdown = lazy(() => import("./MathMarkdown"));

const CODE = /(```[\s\S]*?```|`[^`\n]*`)/g;
const MATH = /\$|\\\(|\\\[/;

export const markdownComponents: Components = {
  pre: ({ children, ...props }) => (
    <pre {...props} tabIndex={0}>
      {children}
    </pre>
  ),
};

/**
 * Rewrites the LaTeX delimiters used in course readings, \( \) for inline math and \[ \] on their own
 * lines for display math, into the dollar forms that remark-math parses. Code spans and blocks are
 * left untouched, so a backslash-parenthesis in an example program stays literal.
 */
export function normalizeMathDelimiters(markdown: string): string {
  return markdown
    .split(CODE)
    .map((part, index) =>
      index % 2 === 1
        ? part
        : part
            .replace(
              /^([ \t]*)\\\[([\s\S]*?)\\\][ \t]*$/gm,
              (_match, indent: string, body: string) =>
                `${indent}$$\n${indent}${body.trim()}\n${indent}$$`,
            )
            .replace(
              /\\\(([\s\S]*?)\\\)/g,
              (_match, body: string) => `$${body}$`,
            ),
    )
    .join("");
}

/** True when prose outside code contains math delimiters, so the KaTeX chunk is worth loading. */
export function containsMath(markdown: string): boolean {
  return markdown
    .split(CODE)
    .some((part, index) => index % 2 === 0 && MATH.test(part));
}

function PlainMarkdown({ children }: { children: string }) {
  return (
    <Markdown
      skipHtml
      remarkPlugins={[remarkGfm]}
      components={markdownComponents}
    >
      {children}
    </Markdown>
  );
}

export function MarkdownReader({ children }: { children: string }) {
  return (
    <div className="markdown">
      {containsMath(children) ? (
        <Suspense fallback={<PlainMarkdown>{children}</PlainMarkdown>}>
          <MathMarkdown>{normalizeMathDelimiters(children)}</MathMarkdown>
        </Suspense>
      ) : (
        <PlainMarkdown>{children}</PlainMarkdown>
      )}
    </div>
  );
}
