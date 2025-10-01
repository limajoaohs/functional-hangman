(require '[clojure.string :as str])

(def word-list [
    "COMPUTER", "PROGRAMMING", "ALGORITHM", "LIBRARY", "PARADIGM",
    "LANGUAGE", "VARIABLE", "CONSTANT", "FRAMEWORK", "DEVELOPER",
    "ELEPHANT", "GIRAFFE", "HIPPOPOTAMUS", "DOG", "CAT", "BUTTERFLY",
    "PINEAPPLE", "WATERMELON", "STRAWBERRY", "ORANGE", "BANANA",
    "UNIVERSITY", "KNOWLEDGE", "STUDENT", "PROFESSOR", "DISCIPLINE"
])

(defn select-word []
  (rand-nth word-list))

(defn create-initial-state [word]
  {:word word
   :guesses #{}
   :lives 6})

(defn display-word [{:keys [word guesses]}]
  (->> word
       (map #(if (guesses (str %)) % "_"))
       (str/join " ")))

(defn process-guess [game-state guess]
  (let [uc-guess (str/upper-case guess)]
    (if (or (not= 1 (count uc-guess))
            (not (Character/isLetter (first uc-guess)))
            ((:guesses game-state) uc-guess))
      game-state
      (let [new-guesses (conj (:guesses game-state) uc-guess)]
        (if (str/includes? (:word game-state) uc-guess)
          (assoc game-state :guesses new-guesses)
          (-> game-state
              (assoc :guesses new-guesses)
              (update :lives dec)))))))

(defn game-status [{:keys [word guesses lives]}]
  (cond
    (<= lives 0) :loss
    (every? #(guesses (str %)) word) :win
    :else :ongoing))

(defn print-game-state [game-state]
  (println "\nWord:" (display-word game-state))
  (println "Lives left:" (:lives game-state))
  (println "Guesses so far:" (str/join ", " (sort (:guesses game-state)))))

(defn get-user-input []
  (print "Enter your guess (a single letter): ")
  (flush)
  (read-line))

(defn print-game-over-message [status word]
  (if (= status :win)
    (println "\n🎉 Congratulations! You guessed the word:" word)
    (println "\n😥 Game Over! The word was:" word)))

(defn game-loop [current-state]
  (let [status (game-status current-state)]
    (if (= status :ongoing)
      (do
        (print-game-state current-state)
        (let [guess (get-user-input)
              next-state (process-guess current-state guess)]
          (recur next-state)))
      (print-game-over-message status (:word current-state)))))

(defn -main [& args]
  (println "--- Welcome to Functional Hangman (Clojure)! ---")
  (-> (select-word)
      (create-initial-state)
      (game-loop)))

(-main)