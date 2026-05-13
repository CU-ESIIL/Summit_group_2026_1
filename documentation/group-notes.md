# Group Notes

Use this shared notebook to capture meeting highlights, decisions, and follow-up tasks.

- Summarize key takeaways after each working session.
- Note data sources, analysis ideas, and open questions.
- Assign owners and due dates for action items so nothing slips through the cracks.
- Drop helpful links, screenshots, or file references so the team can find them later.

Feel free to add new sections as needed to keep everyone aligned and informed.

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
