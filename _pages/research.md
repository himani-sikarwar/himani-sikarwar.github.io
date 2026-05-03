---
permalink: /research/
title: "Research"
author_profile: true
read_time: false
header:
  overlay_image: /images/research-hero.jpg
  overlay_color: "#16213a"
  overlay_opacity: 0.45
---

<style>
.research-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1em;
  margin: 2em 0;
}

.research-grid figure {
  flex: 1 1 calc(50% - 0.5em);
  min-width: 260px;
  opacity: 0;
  transform: translateY(18px);
  animation: fade-up 0.7s ease-out forwards;
}

.research-grid figure:nth-of-type(1) {
  animation-delay: 0.1s;
}

.research-grid figure:nth-of-type(2) {
  animation-delay: 0.2s;
}

.research-grid figure img {
  width: 100%;
  height: auto;
}

.research-highlight {
  padding: 1.5em;
  border-radius: 1rem;
  border: 1px solid var(--global-border-color);
  background: var(--global-background-color);
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.05);
  margin: 2em 0;
  animation: fade-up 0.7s ease-out forwards;
}

@keyframes fade-up {
  from {
    opacity: 0;
    transform: translateY(18px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media screen and (max-width: 720px) {
  .research-grid {
    flex-direction: column;
  }
}
</style>

Welcome to the research hub. This page showcases the key themes, projects, and impact areas that shape my work in security, privacy, and trusted systems for cyber-physical infrastructures.

## Research focus

My current research centers on designing robust, resource-efficient systems for secure Internet of Things, vehicular networks, and next-generation embedded devices.

Key areas of focus:

- **PUF-based hardware security** for lightweight authentication and secure key provisioning.
- **IoT/IoV privacy** through adaptive, data-aware protections and anonymization.
- **AI-enabled security monitoring** that detects anomalous behavior without compromising performance.
- **Trustworthy distributed systems** for edge and cyber-physical environments.

<div class="research-highlight">

### Why this matters

Modern academic and industrial systems increasingly depend on networked devices that are both resource constrained and safety critical. My research aims to make these systems more resilient by combining hardware-rooted trust with software-aware analytics.

</div>

## Selected projects

<div class="research-grid">
  <figure>
    <img src="/images/project-iot-security.jpg" alt="IoT security research" />
    <figcaption>Secure firmware updates and lightweight authentication for IoT devices.</figcaption>
  </figure>

  <figure>
    <img src="/images/project-vehicular-networks.jpg" alt="Vehicular network research" />
    <figcaption>Privacy-preserving coordination for connected cars and edge systems.</figcaption>
  </figure>
</div>

## Research approach

I follow an applied research process that blends theory, system design, and empirical validation:

1. Identify real-world threat models and deployment constraints.
2. Develop hardware-software co-design techniques to minimize overhead.
3. Prototype and evaluate using representative devices, datasets, and simulation.
4. Publish findings with open-source artifacts and reproducible results.

## Highlights and outcomes

- Developed novel PUF-based schemes for secure on-device identity.
- Published peer-reviewed articles on privacy and reliability in IoT systems.
- Built demonstrators for secure connected mobility and autonomous sensing.

## Visual gallery

<figure class="half">
  <img src="/images/research-diagram-1.png" alt="Research architecture diagram" />
  <figcaption>Architecture for secure edge analytics.</figcaption>
</figure>

<figure class="half">
  <img src="/images/research-lab.jpg" alt="Research lab setup" />
  <figcaption>Experimental evaluation with hardware prototypes.</figcaption>
</figure>

## Next steps

If you want to explore specific publications, ongoing projects, or collaborations, please connect through my CV or contact section.

*Note: Replace the placeholder images with your own research visuals by adding them to the `/images/` directory and updating the paths above.*
