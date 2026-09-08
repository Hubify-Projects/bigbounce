interface LabMarkProps {
  size?: number;
  title?: string;
  className?: string;
}

/**
 * BigBounce Lab mark: disc + pupil (singularity) expanding into a sixteen-dot
 * fan (cosmos). Redrawn from site/src/app/icon.svg per hubify BRAND_SYSTEM.md
 * §7 — transparent ground, currentColor throughout, rounded-square container
 * dropped (that belongs to the favicon, not the inline mark). Dots sit on the
 * source's 4px grid so the fan reads balanced from 20px to 96px.
 */
export function LabMark({ size = 24, title, className }: LabMarkProps) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 64 64"
      fill="none"
      className={className}
      role={title ? "img" : undefined}
      aria-hidden={title ? undefined : true}
    >
      {title ? <title>{title}</title> : null}
      <path
        fillRule="evenodd"
        clipRule="evenodd"
        fill="currentColor"
        d="M10,32 A10,10 0 1 0 30,32 A10,10 0 1 0 10,32 Z M16,32 A4,4 0 1 0 24,32 A4,4 0 1 0 16,32 Z"
      />
      <g fill="currentColor">
        <circle cx="34" cy="32" r="1.6" />
        <circle cx="38" cy="28" r="1.4" />
        <circle cx="38" cy="36" r="1.4" />
        <circle cx="42" cy="24" r="1.2" />
        <circle cx="42" cy="32" r="1.2" />
        <circle cx="42" cy="40" r="1.2" />
        <circle cx="46" cy="20" r="1" />
        <circle cx="46" cy="28" r="1" />
        <circle cx="46" cy="36" r="1" />
        <circle cx="46" cy="44" r="1" />
        <circle cx="50" cy="24" r="0.9" />
        <circle cx="50" cy="32" r="0.9" />
        <circle cx="50" cy="40" r="0.9" />
        <circle cx="54" cy="28" r="0.7" />
        <circle cx="54" cy="36" r="0.7" />
        <circle cx="58" cy="32" r="0.6" />
      </g>
    </svg>
  );
}
