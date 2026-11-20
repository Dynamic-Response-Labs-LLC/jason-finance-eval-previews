# J.A.S.O.N. Finance, Lending & Fraud Evaluation Previews

Free, synthetic preview records from [Dynamic Response Labs](https://dynamicresponse.ai) for people who test AI assistants in finance, lending, servicing and fraud-response settings.

Everything is fictional. No real customer or account data. Not a benchmark, not a certification, not professional advice.

## What is here

| File | Records | Contents |
| --- | --- | --- |
| `data/volume_previews.jsonl` | 9 | One compact preview per DRL volume (lockouts, lending and debt resolution, private banking, corporate treasury, vulnerable-adult exploitation, government levies, cyber-extortion and deepfake fraud, BNPL debt, financial de-platforming). Mostly scope previews, not full conversations. |
| `data/scenario_examples.jsonl` | 4 | Short written scenarios with context, a user message, and what a careful response should and should not do. |
| `load_example.py` | | Ten lines that load and print the records. No dependencies. |

The same files are on Hugging Face: https://huggingface.co/datasets/Dynamicresponselabs/JASON-Finance-Lending-Previews

## Try it

```bash
python load_example.py
```

## Using the records

Use them to look at the format, try out a loader or a review sheet, or talk about failure modes with a model-risk or QA team. They are too small to rank models, and doing well on them says nothing about safety, compliance or readiness.

## License

CC BY 4.0 (these records were first published under CC BY 4.0 on Hugging Face in September 2026). Credit "Dynamic Response Labs LLC" and link https://dynamicresponse.ai. See [TERMS.md](TERMS.md).

## More

Full volumes (144 conversations each) are available on request for evaluation. Catalog: https://dynamicresponse.ai/privatedatasetrelease . Questions, or a preview of a specific volume: peter@dynamicresponse.ai

Technical report: https://doi.org/10.5281/zenodo.23002126

