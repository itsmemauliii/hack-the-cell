# Hack the Cell: Solving Real-World Problems with Biology

> Biology is the original operating system, DNA is code, cells are compute, evolution is version control. We're just… finally reading the docs.

---

## Inspiration
We face urgent crises—contaminated water, antibiotic resistance, and microplastics in ecosystems. What if we treated cells like programmable machines and used them to fix problems directly? **Hack the Cell** merges synthetic biology with modern software to create solutions that are innovative, ethical, and deployable.

---

## What it does
**Hack the Cell** is a biosensor platform that:
- Engineers *E. coli* to detect heavy metals in water.
- Uses a Raspberry Pi-based reader to measure fluorescence over time.
- Sends readings to a backend API for analysis.
- Displays real-time results in a Streamlit dashboard, flagging "Safe" or "Unsafe" samples.

---

## How we built it
1. **Wet Lab** – Designed and built a gene circuit with a metal-sensitive promoter and GFP reporter.
2. **Hardware** – Raspberry Pi + Arduino + 3D-printed chassis for low-cost fluorescence measurement.
3. **Backend** – FastAPI service that applies Hill-equation modeling to estimate contaminant concentration.
4. **Frontend** – Streamlit dashboard for uploading CSV data and visualizing results.
5. **Deployment** – Dockerized services; deployable to AWS, GCP, Render, or Streamlit Cloud.

---

## Challenges we ran into
- Leaky gene expression → fixed with tighter repressors and degradation tags.
- Variability in biosensor results → added calibration controls.
- Hardware optical interference → redesigned light path with emission filters.
- Regulatory constraints → confined all work to BSL-1 with strict containment.

---

## Accomplishments we're proud of
- Achieved accurate detection of heavy metals at environmentally relevant concentrations.
- Built a functional low-cost reader from off-the-shelf components.
- Created a full-stack system combining biology, hardware, and software.
- Designed with safety and ethics as core requirements.

---

## What we learned
- Biological systems are inherently variable; embrace and model uncertainty.
- UX matters in scientific tools; make data visualizations intuitive.
- Interdisciplinary skills multiply impact.

---

## What's next
- Multiplex sensors for multiple pollutants.
- Offline inference mode for rural or low-connectivity areas.
- Community-led water monitoring pilots.
- Open-source hardware + software toolkit.

---

## Built With
**Python, R, JavaScript/TypeScript, HTML5/CSS3, FastAPI, Streamlit, NumPy, SciPy, scikit-learn, PyMC, Pandas, Matplotlib, Plotly, AWS (Lambda, S3), GCP (Cloud Run, Storage), Docker, GitHub Actions, PostgreSQL, MinIO/S3, Parquet/Arrow, NCBI Entrez API, UniProt API, Raspberry Pi, Arduino, 3D printing, SnapGene, Benchling, RBS Calculator.**

---

## Deployment

You can deploy with:

* **Streamlit Cloud** – for the dashboard
* **Render / Railway** – for both backend & frontend
* **AWS ECS / GCP Cloud Run** – using Docker

---

## License

MIT License – see [LICENSE](LICENSE) file for details.

