import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";

export function MarkdownReader({ children }: { children: string }) {
  return (
    <div className="markdown">
      <Markdown
        skipHtml
        remarkPlugins={[remarkGfm]}
        components={{
          pre: ({ children, ...props }) => (
            <pre {...props} tabIndex={0}>
              {children}
            </pre>
          ),
        }}
      >
        {children}
      </Markdown>
    </div>
  );
}
