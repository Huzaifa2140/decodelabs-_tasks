Project 1 — Rule-Based Chatbot

I'm teaching a bot to talk using fixed rules, no AI learning involved. User types something → code cleans it up (lowercase, trim spaces) → looks it up in a dictionary of known replies → if found, replies; if not, says "I don't understand" → loops forever until user types bye/exit. That's it. Point of the project: show I can build clean control flow (loops + dictionaries) before touching real AI.
<br>

Project 2 — Iris Classifier (KNN)

I'm teaching a model to guess a flower's species from its measurements. Load 150 flower samples → scale the numbers so they're on the same range → split into 80% train / 20% test → train a KNN model (it predicts a new flower's species by checking its 5 closest neighbors in the training data and taking a majority vote) → test it on the unseen 20% → print accuracy + confusion matrix to prove it actually works. Point of the project: show I can do the basic supervised learning pipeline — load, split, train, predict, evaluate.
<br>

Project 3 — Tech Stack Recommender

I'm matching a user's skills to the best-fit job role. I take 3 skills as input → convert all job roles' required skills and the user's skills into number vectors using TF-IDF (so rare/specific skills count more than generic ones) → calculate cosine similarity between the user's vector and every job role's vector → sort by score and show the top 3 best matches. Point of the project: build a basic content-based recommendation engine using similarity math, the same core idea behind Netflix/Amazon recommendations.
<br>

Project 4 — OCR Text Recognition

I'm building a script that reads text out of an image. The image first goes through pre-processing — grayscale conversion, blur to remove noise, and thresholding to turn it into clean black-and-white — since OCR works way better on clean images than raw ones. Then I run it through Tesseract's OCR engine, which extracts the text along with a confidence score for each word. I only treat the result as reliable if the average confidence is 80% or higher. Point of the project: integrate a pre-trained AI library (Tesseract) into a working pipeline instead of training a model from scratch.
