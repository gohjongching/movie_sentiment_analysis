## Pipeline
### SVM Model: 
Since this is a binary classification task, *Linear Support Vector Machine (SVM)* is used.

![plot](/images/linear_SVM.png)

1. Nonlinear Separability: Movies often contain complex and nuanced language that expresses a wide range of sentiments. SVMs can handle nonlinear separability, meaning they can capture intricate relationships between words and sentiments, allowing them to effectively classify complex text data.

2. High-Dimensional Data: Text data in sentiment analysis is usually high-dimensional, with many features (words) contributing to the overall sentiment. SVMs can handle high-dimensional data and are capable of finding optimal hyperplanes for classification in such spaces.

3. Effective Feature Extraction: SVMs work well with both sparse and dense feature spaces. In movie sentiment analysis, features are often extracted from text through techniques like TF-IDF or word embeddings. SVMs can make accurate predictions using these extracted features.

4. Regularization: SVMs include a regularization parameter that helps prevent overfitting, a common concern in sentiment analysis. Regularization ensures that the model generalizes well to new, unseen data and prevents it from fitting noise in the training data.

5. Binary Classification: Sentiment analysis often involves binary classification (positive/negative). SVMs are inherently designed for binary classification tasks and work well in cases where there are two distinct classes with a clear decision boundary.

6. Small Dataset Effectiveness: In many cases, movie sentiment analysis datasets may not be as large as other datasets. SVMs can still perform well with a smaller dataset size, making them suitable when you don't have access to massive amounts of labeled data.

### TF-IDF Vectorizer: 