interface DiscoveryCardProps {
  title: string;
  children: React.ReactNode;
  tag?: string;
  borderColor?: string;
}

export function DiscoveryCard({
  title,
  children,
  tag,
  borderColor = "#22c55e",
}: DiscoveryCardProps) {
  return (
    <div
      className="card"
      style={{ borderLeft: `3px solid ${borderColor}` }}
    >
      <h4 style={{ margin: "0 0 6px", fontSize: 14, fontWeight: 600 }}>
        {title}
      </h4>
      <p style={{ margin: 0, fontSize: 13, color: "var(--text-secondary)" }}>
        {children}
      </p>
      {tag && (
        <div
          style={{
            marginTop: 8,
            fontSize: 12,
            fontFamily: "var(--font-mono-stack)",
            color: "var(--text-tertiary)",
          }}
        >
          {tag}
        </div>
      )}
    </div>
  );
}
