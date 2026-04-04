interface FeedItemProps {
  date: string;
  title: string;
  children: React.ReactNode;
  tags?: string[];
  type?: "default" | "milestone" | "positive" | "negative" | "active";
}

export function FeedItem({
  date,
  title,
  children,
  tags,
  type = "default",
}: FeedItemProps) {
  return (
    <div className={`feed-item ${type === "default" ? "" : type}`}>
      <div className="feed-date">{date}</div>
      <div className="feed-title">{title}</div>
      <p className="feed-body">{children}</p>
      {tags && tags.length > 0 && (
        <div className="feed-tags">
          {tags.map((tag) => (
            <span key={tag} className="feed-tag">
              {tag}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}
