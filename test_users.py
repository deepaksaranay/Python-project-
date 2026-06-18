class TestUsersAPI:

    def test_get_all_users(self, client):
        res = client.get("/users")
        assert res.status_code == 200
        assert len(res.json()) == 10

    def test_user_schema(self, client):
        """Validate response schema has required keys"""
        res = client.get("/users/1")
        user = res.json()
        required_keys = ["id", "name", "username", "email", "address"]
        for key in required_keys:
            assert key in user, f"Missing key: {key}"

    def test_filter_posts_by_user(self, client):
        """GET posts filtered by userId"""
        res = client.get("/posts", params={"userId": 1})
        assert res.status_code == 200
        posts = res.json()
        assert all(p["userId"] == 1 for p in posts)
