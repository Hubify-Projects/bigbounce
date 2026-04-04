import type { Metadata } from "next";

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
          Non-Technical Explainer &middot; March 2026
        </p>
        <h1>The Big Bounce, Explained</h1>
        <p className="subtitle">
          What if the Big Bang wasn&apos;t the beginning? A plain-English guide
          to why we think the universe bounced.
        </p>
      </div>

      <hr />

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
          No singularity. No infinite density. No breakdown of physics. Just
          a transition from contraction to expansion, governed by physics we
          can test.
        </p>
      </section>

      <section className="section">
        <h2>How Do We Test This?</h2>
        <p>
          The bounce and inflation make different predictions about what we
          should see in the sky today. Our research program has identified the
          key discriminators:
        </p>
        <div className="grid grid-2">
          <div className="card">
            <h3>
              f<sub>NL</sub> = &minus;35/8
            </h3>
            <p>
              The bounce predicts a specific pattern in how galaxies cluster —
              a &ldquo;non-Gaussianity&rdquo; signal of exactly &minus;4.375.
              Inflation predicts this number should be nearly zero. NASA&apos;s
              SPHEREx mission (~2028) will measure this directly.
            </p>
          </div>
          <div className="card">
            <h3>Dark Energy Dynamics</h3>
            <p>
              Our analysis shows 98.6% probability that dark energy changes
              over time (quintom-B behavior). This is exactly what the quintom
              bounce predicts — and something basic inflation cannot explain.
            </p>
          </div>
          <div className="card">
            <h3>Gravitational Wave Hum</h3>
            <p>
              NANOGrav detected a cosmic gravitational wave background. The
              bounce predicts a specific spectral shape (&gamma; = 3.0). The
              measured value is 3.2 &plusmn; 0.6 — perfectly consistent.
            </p>
          </div>
          <div className="card">
            <h3>328,000 Anomalies</h3>
            <p>
              Our AI pipelines have scanned 33.5 million astronomical sources
              across 8 surveys, finding 328,000 objects that don&apos;t match
              known patterns. These anomalies help improve our f<sub>NL</sub>{" "}
              measurement by 6.1%.
            </p>
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
