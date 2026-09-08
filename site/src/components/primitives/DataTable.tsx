import type { ReactNode } from "react";
import { cn } from "@/lib/utils";

export interface DataTableColumn<T> {
  key: string;
  header: string;
  render?: (row: T, index: number) => ReactNode;
  accessor?: (row: T) => ReactNode;
  mono?: boolean;
  align?: "left" | "right";
}

export interface DataTableProps<T> {
  columns: DataTableColumn<T>[];
  rows: T[];
  dense?: boolean;
  stickyHeader?: boolean;
  className?: string;
  rowKey?: (row: T, index: number) => string | number;
  emptyLabel?: string;
}

/**
 * The one bordered list surface in the redesign (REDESIGN_SPEC.md §4.3,
 * §5.1 #6). Used by /papers, /status, /reproduce, /reviews,
 * /docs/architecture, surveys. Put a `<Link>` inside a cell via `render`
 * for a clickable row — DataTable itself stays a plain server-renderable
 * table, no client-side row navigation.
 */
export function DataTable<T>({
  columns,
  rows,
  dense,
  stickyHeader,
  className,
  rowKey,
  emptyLabel = "Nothing to show.",
}: DataTableProps<T>) {
  return (
    <div className="data-table-wrap">
      <table className={cn("data-table", dense && "data-table-dense", className)}>
        <thead>
          <tr>
            {columns.map((c) => (
              <th key={c.key} className={c.align === "right" ? "align-right" : undefined}>
                {c.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.length === 0 && (
            <tr>
              <td colSpan={columns.length} className="data-table-empty">
                {emptyLabel}
              </td>
            </tr>
          )}
          {rows.map((row, i) => (
            <tr key={rowKey ? rowKey(row, i) : i}>
              {columns.map((c) => (
                <td
                  key={c.key}
                  className={cn(c.mono && "mono", c.align === "right" && "align-right")}
                >
                  {c.render
                    ? c.render(row, i)
                    : c.accessor
                      ? c.accessor(row)
                      : String((row as Record<string, unknown>)[c.key] ?? "")}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
