import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { cn } from "@/lib/utils";

type FeedType =
  | "default"
  | "milestone"
  | "positive"
  | "negative"
  | "active";

interface FeedItemProps {
  date: string;
  title: string;
  children: React.ReactNode;
  tags?: string[];
  type?: FeedType;
}

const borderClass: Record<FeedType, string> = {
  default: "border-l-border",
  milestone: "border-l-blue-500",
  positive: "border-l-emerald-500",
  negative: "border-l-red-500",
  active: "border-l-amber-500",
};

const dateClass: Record<FeedType, string> = {
  default: "text-muted-foreground",
  milestone: "text-blue-600 dark:text-blue-400",
  positive: "text-emerald-600 dark:text-emerald-400",
  negative: "text-red-600 dark:text-red-400",
  active: "text-amber-600 dark:text-amber-400",
};

export function FeedItem({
  date,
  title,
  children,
  tags,
  type = "default",
}: FeedItemProps) {
  return (
    <Card className={cn("border-l-4", borderClass[type])}>
      <CardContent className="space-y-2 p-5">
        <div
          className={cn(
            "font-mono text-xs uppercase tracking-wider",
            dateClass[type],
          )}
        >
          {date}
        </div>
        <div
          className="text-base font-semibold leading-snug"
          style={{ fontFamily: "var(--font-serif)" }}
        >
          {title}
        </div>
        <p className="text-sm leading-relaxed text-muted-foreground">
          {children}
        </p>
        {tags && tags.length > 0 && (
          <div className="flex flex-wrap gap-1.5 pt-1">
            {tags.map((tag) => (
              <Badge key={tag} variant="outline" className="text-xs">
                {tag}
              </Badge>
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
