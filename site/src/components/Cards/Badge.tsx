type BadgeVariant =
  | "green"
  | "blue"
  | "amber"
  | "red"
  | "gray"
  | "purple"
  | "accent"
  | "neutral";

interface BadgeProps {
  variant?: BadgeVariant;
  children: React.ReactNode;
}

export function Badge({ variant = "neutral", children }: BadgeProps) {
  return <span className={`badge badge-${variant}`}>{children}</span>;
}
