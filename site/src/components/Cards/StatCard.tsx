interface StatCardProps {
  value: string;
  label: string;
  color?: "green" | "blue" | "amber" | "red";
}

export function StatCard({ value, label, color = "green" }: StatCardProps) {
  return (
    <div className={`status-stat ${color}`}>
      <div className="num">{value}</div>
      <div className="label">{label}</div>
    </div>
  );
}
