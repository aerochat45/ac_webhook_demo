from flask import Flask, jsonify

app = Flask(__name__)

# Dummy member data
MEMBERS = {
    "M001": {
        "name": "Alva Chew",
        "email": "alva.chew@example.com",
        "loyalty_points": 980,
        "membership_level": "Gold"
    },
    "M002": {
        "name": "Gigi",
        "email": "gigi@example.com",
        "loyalty_points": 450,
        "membership_level": "Silver"
    },
    "M003": {
        "name": "Nishant Singh",
        "email": "nishant.singh@example.com",
        "loyalty_points": 1250,
        "membership_level": "Platinum"
    },
    "M004": {
        "name": "Arun",
        "email": "arun@example.com",
        "loyalty_points": 300,
        "membership_level": "Bronze"
    },
    "M005": {
        "name": "John Tan",
        "email": "john.tan@example.com",
        "loyalty_points": 720,
        "membership_level": "Silver"
    },
    "M006": {
        "name": "Meera Patel",
        "email": "meera.patel@example.com",
        "loyalty_points": 1100,
        "membership_level": "Gold"
    },
    "M007": {
        "name": "Daniel Lee",
        "email": "daniel.lee@example.com",
        "loyalty_points": 250,
        "membership_level": "Bronze"
    },
    "M008": {
        "name": "Sophia Wong",
        "email": "sophia.wong@example.com",
        "loyalty_points": 860,
        "membership_level": "Gold"
    },
    "M009": {
        "name": "Rahul Mehta",
        "email": "rahul.mehta@example.com",
        "loyalty_points": 540,
        "membership_level": "Silver"
    },
    "M010": {
        "name": "Emily Brown",
        "email": "emily.brown@example.com",
        "loyalty_points": 1400,
        "membership_level": "Platinum"
    }
}


@app.route("/api/loyalty/<member_id>", methods=["GET"])
def get_loyalty_by_member_id(member_id):
    member = MEMBERS.get(member_id)

    if not member:
        return jsonify({
            "success": False,
            "message": "Member not found"
        }), 404

    return jsonify({
        "success": True,
        "member_id": member_id,
        "data": member
    })


if __name__ == "__main__":
    app.run(debug=True)
