import sys

print("=== Player Score Analytics ===")
if (len(sys.argv) < 2):
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> "
          "<score2> ...")
else:
    scores = []
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            scores.append(0)
    print(f"Scores processed: {scores}")
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))
