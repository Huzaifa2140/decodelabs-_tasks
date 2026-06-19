Project 1 — Rule-Based Chatbot

I'm teaching a bot to talk using fixed rules, no AI learning involved. User types something → code cleans it up (lowercase, trim spaces) → looks it up in a dictionary of known replies → if found, replies; if not, says "I don't understand" → loops forever until user types bye/exit. That's it. Point of the project: show I can build clean control flow (loops + dictionaries) before touching real AI.
<br>
Project 2 — Iris Classifier (KNN)

I'm teaching a model to guess a flower's species from its measurements. Load 150 flower samples → scale the numbers so they're on the same range → split into 80% train / 20% test → train a KNN model (it predicts a new flower's species by checking its 5 closest neighbors in the training data and taking a majority vote) → test it on the unseen 20% → print accuracy + confusion matrix to prove it actually works. Point of the project: show I can do the basic supervised learning pipeline — load, split, train, predict, evaluate.
