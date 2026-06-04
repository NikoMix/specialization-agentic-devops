import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// ─── Site URL & base path ─────────────────────────────────────────────────────
// On GitHub Actions, GITHUB_REPOSITORY is "owner/repo" and GITHUB_REPOSITORY_OWNER
// is just "owner". We derive both `site` and `base` from these so a freshly-forked
// template builds correctly with no manual configuration.
//
// You can override either by setting ASTRO_SITE / ASTRO_BASE as repo variables.
//
// Special case: user/org pages (repo named `<owner>.github.io`) are served from
// the domain root and must use base "/".
const repo = process.env.GITHUB_REPOSITORY ?? 'YOUR_ORG/specialization-agentic-devops';
const [owner, repoName] = repo.split('/');
const isUserOrOrgPage = repoName?.toLowerCase() === `${owner?.toLowerCase()}.github.io`;

const site =
  process.env.ASTRO_SITE ??
  (isUserOrOrgPage ? `https://${owner}.github.io` : `https://${owner}.github.io/${repoName}`);

const base = process.env.ASTRO_BASE ?? (isUserOrOrgPage ? '/' : `/${repoName}/`);

const githubUrl = process.env.ASTRO_GITHUB_URL ?? `https://github.com/${repo}`;

export default defineConfig({
  site,
  base,
  integrations: [
    starlight({
      title: 'Agentic DevOps – Advanced Specialization',
      description:
        'Partner enablement toolkit for the Agentic DevOps Advanced Specialization audit and customer engagement lifecycle.',
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: githubUrl,
        },
      ],
      sidebar: [
        { label: 'Home', link: '/' },
        { label: 'Overview', link: '/overview/' },
        { label: 'Pre-Qualification Requirements', link: '/requirements/' },
        { label: 'Audit Process', link: '/audit-process/' },
        {
          label: 'Module A – General Requirements',
          items: [{ autogenerate: { directory: 'module-a' } }],
        },
        {
          label: 'Module B – Agentic DevOps',
          items: [{ autogenerate: { directory: 'module-b' } }],
        },
        {
          label: 'Engagement Playbook',
          items: [
            { label: 'Offering One-Pager', link: '/engagement/offering-one-pager/' },
            { label: 'Qualification Questionnaire', link: '/engagement/qualification-questionnaire/' },
            { label: 'Discovery Workshop Kit', link: '/engagement/discovery-workshop/' },
            { label: 'WAF Assessment', link: '/engagement/waf-assessment/' },
            { label: 'Assessment Platform Inputs', link: '/engagement/assessment-platform-inputs/' },
            { label: 'Reference Architectures', link: '/engagement/reference-architectures/' },
            {
              label: 'Customer Deliverable Templates',
              items: [{ autogenerate: { directory: 'engagement/deliverables' } }],
            },
            { label: 'Definition of Done', link: '/engagement/definition-of-done/' },
          ],
        },
        {
          label: 'Innersource',
          items: [
            { label: 'Contributing', link: '/innersource/contributing/' },
            { label: 'Content Governance', link: '/innersource/content-governance/' },
            { label: 'Roadmap & Backlog', link: '/innersource/roadmap/' },
          ],
        },
        { label: 'Evidence Tracker', link: '/evidence-tracker/' },
        { label: 'FAQ', link: '/faq/' },
      ],
      editLink: {
        baseUrl: `${githubUrl}/edit/main/`,
      },
    }),
  ],
});
