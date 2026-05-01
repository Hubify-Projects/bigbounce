import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "button-ui inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md border text-sm font-medium no-underline transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default:
          "border-[var(--accent)] bg-[var(--accent)] text-white shadow-sm hover:bg-[var(--accent-dim)]",
        destructive:
          "border-[var(--crit)] bg-[var(--crit)] text-white shadow-sm hover:opacity-90",
        outline:
          "border-[var(--border)] bg-[var(--surface)] text-[var(--text)] shadow-sm hover:border-[var(--border-bright)] hover:bg-[var(--surface-2)]",
        secondary:
          "border-[var(--border)] bg-[var(--surface-2)] text-[var(--text)] shadow-sm hover:bg-[var(--surface-3)]",
        ghost: "border-transparent hover:bg-[var(--surface-2)] hover:text-[var(--text)]",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "min-h-10 px-5 py-2",
        sm: "min-h-9 px-4 py-2 text-xs",
        lg: "min-h-11 px-7 py-2.5",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  },
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        data-variant={variant ?? "default"}
        data-size={size ?? "default"}
        ref={ref}
        {...props}
      />
    );
  },
);
Button.displayName = "Button";

export { Button, buttonVariants };
