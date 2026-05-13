# Project Group Template

This repository is a template for ESIIL Project Groups.

The website is built from the docs/ folder using MkDocs.

# Some Reflections/Summaries After Day 1:
1. We propose that authors in the fields of environmental data science should report on the computational/energy costs associated with their modeling.
2. We create a prototype of a "calculator" for the most common analytical methods within the field to make this reporting process streamlined.

Methods:
1. "Literature review" to show that this is an issue. Demonstrating that it's not currently the norm. This could be a true review, or more of a narrative analysis demonstrating that this is an issue and explaining our rationale for why we think people should care.
2. Calculator prototype.


Questions to answer:
- What do we mean by "environmental data science"? Do we define this by venue/journal? By content? By author affiliation?
- What methods do we want to include in our calculator?
- Do we count genAI assistance as a part of the calculation?
- _Is this more along the lines of a data availability statement/AI reporting OR something that should be reported alongside metrics like R_2 in a results section?_
      I think this is a major distinction that will impact our lit review and framing
- Is this more of a perspective piece?

## Questions about calculator boundaries:
There's lots of literature about data center energy usage that explains that it's hard to come up with a standardized measure because you can draw the boundaries whereever. I think it's important to define things like:
1. If you're fine-tuning a large model, are we counting the energy usage of only the fine-tuning? Or do we consider that the larger model itself took lots of energy to train? Same thing with API calls. _To me, this kind of suggests that putting this alongside performance metrics instead of as mandatory reporting could make more sense. With a direct acknowledgment that there is no perfect, standardized way to do this._
3. Are we considering costs of data storage/hosting too? For huge data, that could be very relevant.
4. Are there ways to also include non-quantitative acknowledgments? Maybe for scope it makes sense to limit it to just environmental impacts that can be quantified, BUT it would be interesting to imagine some looser acknowledgments of transparency/cost/etc. that are all really relevant for reproducibility and democratizing science. 

## Project Questions

Bea's Questions:

    Guardrails: types of datasets, replication and samples sizes we're shooting for
    Outouts: predictive accuracy? Which metrics?


## Preview locally

pip install mkdocs-material
mkdocs serve

## Build site

mkdocs build --strict --clean

## Site Health

The site generates a non-blocking health report during the build.

The report appears at the bottom of the homepage and flags common issues such as missing files, placeholder links, or incomplete template fields.

Warnings do not prevent the site from publishing.

## Editing Pages

Use the edit icon on the website to open the corresponding markdown file in GitHub edit mode.

## Team Profiles

Each person has their own Markdown profile file in `docs/people/`. The homepage People gallery reads those files at build time. Use `docs/_data/people.yml` only as an index of profile paths, for example `profile: people/your-name.md`; do not duplicate profile text in YAML.

## Citations

Add BibTeX entries to `docs/references.bib`, then cite them in Markdown with `[@citationKey]`. The site build renders the References section automatically.

## Completing the Results and Polished Outputs

Use the homepage **Results** and **Polished Outputs** sections as a synthesis checklist, not an activity log. Add specific insights, link each one to a figure, notebook, PDF, dashboard, data product, or other artifact, and mark confidence as High, Medium, or Low with a short reason.

Strong entries state what changed, why it matters, what evidence supports it, what remains uncertain, and what another group can reuse. Keep the text short enough to present in a 2-minute walkthrough.

## GitHub Pages

This site is automatically built and deployed using GitHub Actions.

## License

This template is released under the MIT License.
