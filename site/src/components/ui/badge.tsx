import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const badgeVariants = cva("badge", {
  variants: {
    variant: {
      default: "badge-green",
      neutral: "badge-neutral",
      accent: "badge-accent",
      green: "badge-green",
      blue: "badge-blue",
      amber: "badge-amber",
      red: "badge-red",
      purple: "badge-purple",
      secondary: "badge-neutral",
      destructive: "badge-red",
      outline: "badge-neutral",
    },
  },
  defaultVariants: {
    variant: "default",
  },
});

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  );
}

export { Badge, badgeVariants };
