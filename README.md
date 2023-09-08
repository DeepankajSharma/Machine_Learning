
# Credit Card Fraud Detection using Machine learning 

This project is aimed at developing a machine learning-based solution for detecting credit card fraud. Credit card fraud is a significant issue for financial institutions and cardholders, and accurate detection is crucial to minimize financial losses and protect consumers.

Our solution uses machine learning techniques to analyze credit card transaction data and identify potentially fraudulent transactions. We have employed [Support Vector Machines (SVM)] to achieve this goal. The project focuses on addressing the challenge of class imbalance in the dataset, where fraudulent transactions are rare compared to legitimate ones.

The dataset I've described contains transaction data from credit cards in September 2013, specifically focusing on two days of transactions. Here are the key characteristics and information about this dataset:

1. **Data Distribution:**
   - The dataset includes 284,807 transactions.
   - There are a total of 492 frauds, making the dataset highly unbalanced.
   - Fraudulent transactions (Class 1) account for only 0.172% of all transactions.

2. **Features:**
   - The dataset primarily consists of numerical input variables.
   - The features V1 through V28 are the result of a Principal Component Analysis (PCA) transformation. These are the principal components of the data.
   - The 'Time' feature represents the time elapsed (in seconds) between each transaction and the first transaction in the dataset.
   - The 'Amount' feature represents the transaction amount.
   - The 'Class' feature is the response variable, with a value of 1 indicating a fraudulent transaction and 0 indicating a normal transaction.

3. **Model Choice:**
   - Due to the highly unbalanced nature of the dataset, where frauds are a very small proportion of the data, it is recommended to use evaluation metrics other than accuracy.
   - Accuracy may not be meaningful for unbalanced classification problems like this one.
   - The recommended metric for evaluation is the Area Under the Precision-Recall Curve (AUPRC), which is more suitable for imbalanced datasets.

4. **Model Selection:**
   - Based on your description, Support Vector Machines (SVM) have shown promise in providing good accuracy on test data for credit card fraud detection. SVM is a popular choice for binary classification tasks and can be effective in handling imbalanced data.

this dataset represents credit card transaction data with a severe class imbalance, where the majority of transactions are normal, and a very small percentage are fraudulent. Due to this imbalance, SVM is suggested as a potential model for detecting fraudulent transactions, and the AUPRC should be used to evaluate its performance instead of traditional accuracy metrics.




## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Appendix

Any additional information goes here


## Authors

- [@octokatherine](https://www.github.com/octokatherine)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Demo

Insert gif or link to demo

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## Feedback

If you have any feedback, please reach out to us at fake@fake.com


## FAQ

1. What is the purpose of this Credit Card Fraud Detection project?

   Ans: This project aims to develop a machine learning-based solution for detecting fraudulent credit card transactions to protect both financial institutions and cardholders.

2. What machine learning models are used for fraud detection?

   Ans: We primarily use Support Vector Machines (SVM) have shown promise in providing good accuracy on test data for credit card fraud detection.

3.What evaluation metrics are used to assess the model's performance?

Ans: We use the Area Under the Precision-Recall Curve (AUPRC) as the primary evaluation metric for assessing the model's performance on this highly imbalanced dataset. 
Details about the evaluation:
Train score: {'logistic_regression': 0.7913279132791328, 
'Naive Bayes': 0.92547425474254
74, 
'SVM': 0.93125}
Test score: {'logistic_regression': 0.8089430894308943, 'Naive Bayes': 0.88617886178861
79, 'SVM': 0.9007777777777777}
from above we conclude that SVM(Support vetor machine) give more accuracy on test data so we can say
that we use SVM for credit card fraud Detection

4.Where can I find the dataset used in this project?

Ans: The dataset used for this project is available at Kaggle.

5. How can I get in touch with the project authors for questions or collaboration?

Ans: You can contact us at Gmail: deepankajsharma020@gmail.com  for any inquiries, suggestions, or collaboration opportunities.

If you have any more questions or encounter issues not addressed in this FAQ, please feel free to reach out to us. We're here to help!


 
## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## 🚀 About Me
 

Welcome to my GitHub profile! I'm Deepankaj Sharma, a passionate Data Scientist and Machine Learning enthusiast with a strong background in
Computer Science & engineering.

### What I Do

- 📊 I'm dedicated to turning data into actionable insights. My primary focus is on exploratory data analysis, data mining ,predictive modeling, and machine learning applications.
- 💻 I'm skilled in programming languages such as Python and have experience working with popular libraries like pandas,Numpy ,scikit-learn, TensorFlow, and PyTorch.
- 🧠 I love diving into complex problems and finding innovative solutions using cutting-edge machine learning techniques.
- 📈 I'm a firm believer in the power of data-driven decision-making and enjoy sharing my knowledge through writing and coding.

### Projects

You'll find a collection of my Data Science and Machine Learning projects on my GitHub. These projects showcase my skills in data preprocessing, feature engineering, model development, and more. Feel free to explore them, provide feedback, or collaborate with me on any of them.

### Connect With Me

- 📧 You can reach out to me at [Gmail] (deepankajsharma020@gmail.com)
- 💼 Let's connect on [Linkdin](linkedin.com/in/deepankaj-sharma-55787a202). I'm always open to networking and collaborating on exciting projects.
 

### Stay Curious, Keep Learning

Data Science and Machine Learning are ever-evolving fields, and I'm committed to continuous learning. Let's embark on this journey together and unlock the potential of data-driven solutions.

Feel free to explore my repositories, ask questions, and let's make data science and machine learning more accessible and exciting for everyone!


