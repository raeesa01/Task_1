from flask import Flask, request, jsonify
from get_papers.get_papers_list import fetch_papers

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API is running!"})

@app.route("/papers", methods=["GET"])
def get_papers():
    query = request.args.get("query")
    if not query:
        print("[ERROR] Query parameter is missing.")
        return jsonify({"error": "Missing 'query' parameter"}), 400

    try:
        print(f"[INFO] Fetching papers for query: {query}")
        papers = fetch_papers(query)
        print(f"[INFO] Retrieved {len(papers)} papers.")
        return jsonify(papers)
    except Exception as e:
        print("[ERROR] Exception occurred while fetching papers:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
