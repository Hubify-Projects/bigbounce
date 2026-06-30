import { Separator } from"@/components/ui/separator";
import type { Metadata } from"next";

export const metadata: Metadata = {
  title: "Explainer",
  description:
    "A non-technical explanation of the BigBounce research program.",
};

export default function ExplainedPage() {
  return (
    <>
      <div className="hero">
        <p className="text-xs sans" style={{ marginBottom: 8 }}>
          Non-Technical Explainer &middot; June 2026
        </p>
        <h1 style={{ fontFamily:"var(--font-mono-stack)", fontWeight: 600 }}>
          The Big Bounce, Explained
        </h1>
        <p className="subtitle">
          What if the Big Bang wasn&apos;t the beginning? A plain-English guide
          to why we think the universe bounced.
        </p>
      </div>

      <Separator className="my-8" />

      <section className="section">
        <h2>The Standard Story</h2>
        <p>
          The standard model of cosmology says the universe began with the Big
          Bang — an explosion from an infinitely dense point about 13.8 billion
          years ago. In the first fraction of a second, it underwent
          &ldquo;inflation&rdquo; — an exponential expansion that smoothed
          everything out and set the stage for galaxies, stars, and planets.
        </p>
        <p>
          This story works remarkably well. It explains the cosmic microwave
          background, the abundance of light elements, and the large-scale
          structure of the universe. But it has a problem: the beginning.
        </p>
      </section>

      <section className="section">
        <h2>The Problem with the Beginning</h2>
        <p>
          General relativity — Einstein&apos;s theory of gravity — predicts
          that if you rewind the universe to the Big Bang, you hit a
          &ldquo;singularity&rdquo;: a point of infinite density where the laws
          of physics break down. This isn&apos;t a place or a thing — it&apos;s
          a sign that the theory is incomplete. Something is missing.
        </p>
        <p>
          Inflation tries to explain what happened just after the singularity,
          but it doesn&apos;t explain the singularity itself. It&apos;s like
          describing a car accident in detail but never explaining why the car
          was on the road in the first place.
        </p>
      </section>

      <section className="section">
        <h2>The Bounce Alternative</h2>
        <p>
          Bounce cosmology proposes a different history: instead of a
          singularity, the universe underwent a &ldquo;bounce.&rdquo; A
          previous universe contracted, reached a maximum density (incredibly
          high, but finite), and then rebounded into expansion — what we
          observe as the Big Bang.
        </p>
        <p>
          No singularity. No infinite density. No breakdown of physics. Just a
          transition from contraction to expansion, governed by physics we can
          test.
        </p>
      </section>

      <section className="section">
        <h2>How Do We Test This?</h2>
        <p>
          The bounce and inflation make different predictions about what we
          should see in the sky today. Our research program has identified the
          key discriminators:
        </p>
        <div
          className="mt-4 rounded-lg p-5"
          style={{ background: "color-mix(in srgb, var(--surface-2) 55%, transparent)" }}
        >
          <div className="grid gap-5 md:grid-cols-2">
            <div>
              <p
                className="font-semibold text-sm mb-1"
                style={{ fontFamily: "var(--font-mono-stack)" }}
              >
                f<sub>NL</sub> = &minus;35/8
              </p>
              <p className="text-sm leading-relaxed text-muted-foreground">
                The matter-bounce scenario predicts a specific pattern in how
                galaxies cluster — a &ldquo;non-Gaussianity&rdquo; signal of
                &minus;4.375. Inflation predicts this number should be nearly
                zero. NASA&apos;s SPHEREx mission (~2028) will measure this
                directly.
              </p>
            </div>
            <div>
              <p
                className="font-semibold text-sm mb-1"
                style={{ fontFamily: "var(--font-mono-stack)" }}
              >
                Dark Energy Dynamics
              </p>
              <p className="text-sm leading-relaxed text-muted-foreground">
                Whether dark energy&apos;s strength changes over time is one of
                the open questions the bounce can speak to. The quintom branch
                of bounce cosmology predicts &ldquo;quintom-B&rdquo; behavior
                (the equation of state crosses w = &minus;1). External DESI DR2
                analyses now report 2.8&ndash;4.2σ for w-crossing depending on
                the dataset combination. Our own program treats this
                theoretically — we have not yet run a free-w<sub>0</sub>&ndash;w
                <sub>a</sub> MCMC ourselves; that&apos;s a planned next step.
              </p>
            </div>
            <div>
              <p
                className="font-semibold text-sm mb-1"
                style={{ fontFamily: "var(--font-mono-stack)" }}
              >
                Gravitational Wave Hum
              </p>
              <p className="text-sm leading-relaxed text-muted-foreground">
                NANOGrav detected a cosmic gravitational wave background. The
                bounce predicts a specific spectral shape (&gamma; = 3.0). The
                measured spectral slope (our real free-spectrum re-fit) is 2.567 &plusmn; 0.382 — consistent at +1.13σ, while the black-hole-binary value 4.33 is excluded at +4.61σ.
              </p>
            </div>
            <div>
              <p
                className="font-semibold text-sm mb-1"
                style={{ fontFamily: "var(--font-mono-stack)" }}
              >
                378,280 Anomalies
              </p>
              <p className="text-sm leading-relaxed text-muted-foreground">
                Our AI pipelines have scanned 37.3 million astronomical sources
                across seven surveys, finding 378,280 objects that do not match
                known patterns. These anomalies supply candidate high-bias
                tracers that could sharpen the f<sub>NL</sub> measurement
                (central forecast improvement 9.4%, consistent with zero
                improvement at current signal-to-noise).
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="section">
        <h2>What Happens Next?</h2>
        <p>
          SPHEREx launches around 2028 and will measure f<sub>NL</sub> to a
          precision of about &plusmn;1. If it finds f<sub>NL</sub> near
          &minus;4.375, that&apos;s strong evidence for the bounce. If it
          finds f<sub>NL</sub> near zero, the bounce (in its simplest form) is
          ruled out.
        </p>
        <p>
          In the meantime, we&apos;re squeezing every drop of information from
          current data — improving our measurements, scanning more surveys, and
          building the most complete picture of what the data already tells us.
        </p>
        <p>
          The goal is simple: find out if the universe bounced. The answer
          matters because it tells us whether the cosmos has a beginning, or
          whether it has always existed in some form — contracting, bouncing,
          expanding, and perhaps bouncing again.
        </p>
      </section>
    </>
  );
}
