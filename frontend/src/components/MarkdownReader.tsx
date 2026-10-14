import Markdown from "react-markdown";

export function MarkdownReader({ children }: { children: string }) {
  return (
    <div className="markdown">
      <Markdown
        skipHtml
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
