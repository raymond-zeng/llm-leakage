# llm-leakage

The primary goal of this project is to assess the extent to which evaluation datasets leak into pretraining data and how this affects model performance. Specifically, we aim to answer three main questions. How much do models already “know” about  certain evaluation datasets from pre-training? How much do LLMs improve from seeing evaluation data in training? What level of abstraction (e.g. descriptions, concrete examples, etc.) help models and how much?

This research is important because models that have seen their own evaluation datasets in training may give a false impression of generalization. Understanding leakage effects is crucial for fair and robust benchmarking. Our selected paper \citep{elangovan-etal-2021-memorization} is directly relevant to our project on eval leakage in pretraining because it provides quantitative methods to detect leakage, which we can apply to our fine-tuning experiments. The paper also highlights how test set contamination affects performance, a core concern in our study of benchmark validity. The authors also suggest that even partial exposure to evaluation data can significantly impact model performance, aligning with our experiment on different levels of dataset exposure.  

## NLP Tasks and Data
We will investigate leakage in the context of two primary NLP tasks: QA and coding.

For QA we will evaluate our models on TQA-Bench which is a benchmark that requires LLMs to answer multiple choice questions based on a provided table. For example, given a table of airports and flights, the model may have to answer: "What is the average flight delay at Chicago O'Hare International Airport?" We chose this dataset due to it's recency, so it is unlikely to be contaminated.

We also plan to test on CodeELO which is a benchmark comprised of Codeforces problems. Codeforces is a website that hosts weekly coding competitions. This benchmark is likely contaminated as it contains a multitude of codeforces problems which LLMs have likely been trained on. We also plan to create our own custom dataset using recent codeforces problems which are likely uncontaminated. We speculate that the models will struggle more on our custom codeforces dataset and the fine-tuned models will show greater improvement on our custom dataset compared to the CodeELO dataset.

## Methods and Baselines  
We will analyze two open-source LLMs: Llama3 and DeepSeek R1. We will first see how much knowledge the LLMs have on our evaluation datasets by giving them training samples and asking where the evaluations come from and what they know about the evaluations. We will then fine-tune the models to different levels. We will fine-tune the models on partial data, the full dataset as well as for different number of epochs. We will also use different methods of fine-tuning such as GRPO and training on the samples in the dataset.

Our baseline will be the comparison to base versions of the Llama3 and DeepSeek R1 v2 which we will download from HuggingFace.

## Evaluation
For the QA datasets, we will simply use accuracy as a metric and compare the results between the base models and the fine-tuned models. For the coding datasets, we can also use accuracy by having the models generate C++ code and then submitting the code onto codeforces to evaluate within the time constraints.

We are also curious in a metric called zlib-perplexity ratio which was introduced in "Extracting Training Data from Large Language Models." Zlib measures the number of bits of entropy a text contains when compressed with zlib compression. Thus, the zlib-perplexity ratio can be used to identify memorization and repeated patterns.





