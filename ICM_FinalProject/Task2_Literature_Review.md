# Intro to Comp Med: Imaging — Final Project, Task 2

**Group 1** · Huntington's disease (HD) · Occipital lobe · `HD_ICM_random200.xlsx`

Task 2 asks us to *discuss how the brain region may be involved in the assigned disease and summarize relevant existing literature* (grading: involvement 2 pts, literature 2 pts).

Our ROIs (left and right of each, 10 volumes): cuneus (Cu), lingual gyrus (LG), inferior occipital gyrus (IOG), middle occipital gyrus (MOG), superior occipital gyrus (SOG).

Slides for this task (cover, 3 content slides, references, with speaker notes) are in the Task 2 slide deck. Every claim below and on the slides is tied to a source in the reference list.

---

## 1. Summary

HD is best known as a disease of the striatum, but the mutant protein is made by neurons throughout the brain and the cerebral cortex degenerates too. Among cortical regions, the occipital lobe is one of the earliest and fastest to thin. In TRACK-HD (the study our data come from), occipital thinning appears even before symptoms and predicts worse visual-cognition scores. We therefore expect HD subjects to have smaller occipital volumes than controls, and we test this in Task 4.

---

## 2. The disease in brief

- **Cause.** An expanded CAG trinucleotide repeat in the huntingtin gene (*HTT*, chromosome 4p16.3), inherited in an autosomal dominant pattern [HDCRG 1993]. 36–39 repeats give reduced penetrance; 40 or more give full penetrance [Tabrizi 2020].
- **Hallmark pathology.** Loss of GABAergic medium spiny neurons in the striatum (caudate and putamen) [Tabrizi 2020].
- **Symptoms.** A triad of motor (chorea), cognitive and psychiatric symptoms, usually starting between ages 30 and 50 [HDSA].
- **Silent phase.** Measurable brain and cognitive changes begin roughly 10–20 years before clinical diagnosis [Paulsen 2008].

---

## 3. How the occipital lobe could be involved

1. **The cortex degenerates too, not just the striatum.** Huntingtin is expressed widely [HDCRG 1993]. Post-mortem stereology finds loss of total neurons and pyramidal cells across frontal, parietal, temporal and occipital cortex [Nana 2014].
2. **Thinning moves from back to front.** Cortical thinning starts early and appears to spread from posterior to anterior regions as the disease progresses [Rosas 2002]. In stage I–II patients, sensorimotor, parietal and occipital cortex are already thin, while anterior frontal and temporal regions are relatively spared [Rosas 2008].
3. **The visual cortex is wired into the striatum.** Visual cortex projects to the tail of the caudate through a visual corticostriatal loop [Seger 2013]. Damage at either end of a corticostriatal loop is one proposed route by which striatal and cortical degeneration spread to each other.
4. **Clinical consequences.** People with HD show reduced integrity of the visual pathway and deficits in colour and motion perception [Dhalla 2019]. They also show impaired visual search and mental rotation, which track posterior brain structure [Labuschagne 2016]. Visual deficits matter for daily function and for cognitive tests used in HD trials [Coppen 2018, *Behav Brain Res*].

---

## 4. Literature evidence

| Year | Study | Sample and method | Occipital finding |
|---|---|---|---|
| 2002 | Rosas et al., *Neurology* | 11 HD vs 13 controls; MRI cortical thickness | Thinning occurs early and appears to proceed from posterior to anterior; sensorimotor cortex most affected |
| 2008 | Rosas et al., *Brain* | 33 HD across stages vs 22 controls; MRI cortical thickness | Stage I–II: thinning over sensorimotor, parietal and occipital cortex; anterior frontal and temporal relatively spared. Regional thinning tracks clinical heterogeneity |
| 2014 | Nana et al., *J Huntingtons Dis* | 14 HD vs 15 controls; post-mortem stereology, 6 cortical regions | Neuron and pyramidal-cell loss in every region studied **except primary visual cortex** |
| 2015 | Rüb et al., *Brain Pathol* | 7 HD vs 7 controls; stereology of BA17 (primary visual cortex) | **32% fewer neurons** in BA17 (≈71 vs ≈104 million), mainly in layers III, IV and VI |
| 2015 | Johnson et al., *Neuropsychologia* | TRACK-HD: 97 controls, 109 premanifest, 69 early HD; FreeSurfer thickness of 4 occipital regions | Occipital thickness reduced in **both premanifest and early HD**. Thinner cortex linked to worse performance on 5 of 6 visual tasks, strongest for **lateral occipital and lingual**; **cuneus showed no association**; finger tapping (non-visual) unrelated |
| 2016 | Labuschagne et al., *J Int Neuropsychol Soc* | TRACK-HD: 119 premanifest, 104 early HD, 110 controls | Visual search and mental rotation track parietal and occipital volume and thickness (precuneus, cuneus, calcarine, lingual) and posterior fusiform. Visual search declined over 12 months in early HD |
| 2018 | Coppen et al., *Hum Brain Mapp* | 18 controls, 21 premanifest, 20 manifest; VBM, thickness, resting-state fMRI | Manifest HD: atrophy of associative visual cortex and reduced connectivity of lingual gyrus, occipital pole and occipital fusiform with the medial visual network. **Premanifest: no differences** |
| 2019 | Dhalla et al., *J Huntingtons Dis* | Systematic review | Retinal thinning, reduced VEP amplitude, visual-cortex cell loss and thinning; colour and motion perception deficits |
| 2021 | Johnson et al., *Biol Psychiatry* | 49 HD gene carriers vs 49 controls, 3–7 scans each over 10 years | Widespread cortical differences, but **occipital and parietal regions show the greatest rate of atrophy** |

### Where the literature disagrees (useful for Task 4)

- **Primary visual cortex (V1).** Nana 2014 found V1 spared, while Rüb 2015 found 32% neuron loss in V1. Associative visual cortex (the lateral occipital and lingual regions) is affected more consistently.
- **Premanifest stage.** Johnson 2015 (n = 109 premanifest) found occipital thinning before symptoms, while Coppen 2018 (n = 21 premanifest) did not. The larger study is more likely to detect small early effects.
- **Our dataset.** The spreadsheet labels subjects only as `HD` or `NORMAL`. TRACK-HD and PREDICT-HD both enrolled premanifest gene carriers [Tabrizi 2009; Paulsen 2008]. Our `HD` group is therefore probably a mix of premanifest and early-stage people. If so, our effect sizes should be smaller than in studies of manifest HD only.

---

## 5. Matching literature labels to our ROIs

Most of the imaging studies above use FreeSurfer's Desikan–Killiany labels. Our volumes come from MRICloud's JHU multi-atlas labels, which divide the occipital lobe differently:

| Literature (FreeSurfer) | Our MRICloud ROIs |
|---|---|
| Lateral occipital | IOG, MOG and part of SOG |
| Lingual | LG |
| Cuneus | Cu |
| Pericalcarine (V1, calcarine banks) | No separate label: upper bank in Cu, lower bank in LG |

So when we compare our Task 4 results with Johnson 2015, "lateral occipital" findings should be compared with our IOG and MOG results.

---

## 6. Hypothesis carried into Task 4

- **H1.** HD subjects have smaller volumes than controls in all 10 occipital ROIs, on both sides.
- **H2.** The lingual and lateral occipital gyri (LG, IOG, MOG) are the regions most tied to symptoms, because they have the strongest links to visual-cognition deficits [Johnson 2015; Coppen 2018].

H2 is about clinical relevance, not a prediction that these ROIs show the largest volume differences. The literature does not rank the five gyri by atrophy size.

---

## 7. Speaker script (≈ 80 seconds)

**Slide "Beyond the striatum" (≈ 25 s).**
Huntington's disease is caused by an expanded CAG repeat in the huntingtin gene and is inherited in an autosomal dominant way. Its hallmark is the loss of medium spiny neurons in the striatum. But mutant huntingtin is made by neurons throughout the brain, so the cortex degenerates too, and cortical thinning moves from the back of the brain forward. That includes the visual cortex, which loops into the tail of the caudate. Patients develop problems with colour and motion perception, visual search and mental rotation.

**Slide "Studies since 2002" (≈ 30 s).**
The literature consistently puts the occipital lobe early in the disease. Rosas showed that cortical thinning moves from posterior to anterior, with occipital thinning already present in stage one and two patients. Post-mortem counts confirm neuron loss across the cortex, though studies disagree about the primary visual cortex itself. In TRACK-HD, the study our data come from, Johnson found occipital thinning even before symptoms, and it predicted worse visual-test scores. Over ten years, the occipital and parietal cortex atrophied fastest of any cortical region.

**Slide "What we expect in our 10 occipital ROIs" (≈ 25 s).**
For our ten structures, the lingual gyrus and the lateral occipital gyri, inferior and middle, have the strongest links to visual deficits in HD. The cuneus thins but has not been tied to test scores. So we hypothesise that HD subjects have smaller volumes in all ten occipital ROIs, on both sides, which we test next. One caveat: most studies use FreeSurfer labels, so their "lateral occipital" roughly equals our IOG and MOG, and primary visual cortex is split between our cuneus and lingual gyrus.

---

## 8. References

1. Coppen EM, van der Grond J, Hart EP, Lakke EAJF, Roos RAC. The visual cortex and visual cognition in Huntington's disease: an overview of current literature. *Behav Brain Res.* 2018;351:63–74. doi:10.1016/j.bbr.2018.05.019
2. Coppen EM, et al. Structural and functional changes of the visual cortex in early Huntington's disease. *Hum Brain Mapp.* 2018;39(12):4776–4786. doi:10.1002/hbm.24322
3. Dhalla A, Pallikadavath S, Hutchinson CV. Visual dysfunction in Huntington's disease: a systematic review. *J Huntingtons Dis.* 2019;8(2):233–242. doi:10.3233/JHD-180340
4. The Huntington's Disease Collaborative Research Group. A novel gene containing a trinucleotide repeat that is expanded and unstable on Huntington's disease chromosomes. *Cell.* 1993;72(6):971–983. doi:10.1016/0092-8674(93)90585-E
5. Huntington's Disease Society of America. Overview of Huntington's disease. https://hdsa.org/what-is-hd/overview-of-huntingtons-disease/
6. Johnson EB, et al. The impact of occipital lobe cortical thickness on cognitive task performance: an investigation in Huntington's disease. *Neuropsychologia.* 2015;79(Pt A):138–146. doi:10.1016/j.neuropsychologia.2015.10.033
7. Johnson EB, et al. Dynamics of cortical degeneration over a decade in Huntington's disease. *Biol Psychiatry.* 2021;89(8):807–816. doi:10.1016/j.biopsych.2020.11.009
8. Labuschagne I, Cassidy AM, Scahill RI, et al. Visuospatial processing deficits linked to posterior brain regions in premanifest and early stage Huntington's disease. *J Int Neuropsychol Soc.* 2016;22(6):595–608. doi:10.1017/S1355617716000321
9. Nana AL, Kim EH, Thu DCV, et al. Widespread heterogeneous neuronal loss across the cerebral cortex in Huntington's disease. *J Huntingtons Dis.* 2014;3(1):45–64. doi:10.3233/JHD-140092
10. Paulsen JS, et al. Detection of Huntington's disease decades before diagnosis: the Predict-HD study. *J Neurol Neurosurg Psychiatry.* 2008;79(8):874–880. doi:10.1136/jnnp.2007.128728
11. Rosas HD, Liu AK, Hersch S, et al. Regional and progressive thinning of the cortical ribbon in Huntington's disease. *Neurology.* 2002;58(5):695–701. doi:10.1212/WNL.58.5.695
12. Rosas HD, et al. Cerebral cortex and the clinical expression of Huntington's disease: complexity and heterogeneity. *Brain.* 2008;131(Pt 4):1057–1068. doi:10.1093/brain/awn025
13. Rüb U, et al. Huntington's disease (HD): neurodegeneration of Brodmann's primary visual area 17 (BA17). *Brain Pathol.* 2015;25(6):701–711. doi:10.1111/bpa.12237
14. Seger CA. The visual corticostriatal loop through the tail of the caudate: circuitry and function. *Front Syst Neurosci.* 2013;7:104. doi:10.3389/fnsys.2013.00104
15. Tabrizi SJ, et al. Biological and clinical manifestations of Huntington's disease in the longitudinal TRACK-HD study: cross-sectional analysis of baseline data. *Lancet Neurol.* 2009;8(9):791–801. doi:10.1016/S1474-4422(09)70170-X
16. Tabrizi SJ, Flower MD, Ross CA, Wild EJ. Huntington disease: new insights into molecular pathogenesis and therapeutic opportunities. *Nat Rev Neurol.* 2020;16(10):529–546. doi:10.1038/s41582-020-0389-4

**Further reading (not cited on the slides):** Wolf RC, et al. Visual system integrity and cognition in early Huntington's disease. *Eur J Neurosci.* 2014;40:2417–2426. doi:10.1111/ejn.12575. This study found occipitotemporal atrophy, and its reduced fusiform activity tracked lower SDMT scores.
