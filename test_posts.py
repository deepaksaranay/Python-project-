import pytest

class TestPostsAPI:

    def test_get_all_posts(self, client):
        """GET /posts → 200, returns list of 100"""
        res = client.get("/posts")
        assert res.status_code == 200
        data = res.json()
        assert isinstance(data, list)
        assert len(data) == 100

    def test_get_single_post(self, client):
        """GET /posts/1 → valid structure"""
        res = client.get("/posts/1")
        assert res.status_code == 200
        post = res.json()
        assert "id" in post
        assert "title" in post
        assert "body" in post
        assert post["id"] == 1

    def test_create_post(self, client, sample_post):
        """POST /posts → 201, returns created object"""
        res = client.post("/posts", sample_post)
        assert res.status_code == 201
        created = res.json()
        assert created["title"] == sample_post["title"]
        assert "id" in created

    def test_update_post(self, client, sample_post):
        """PUT /posts/1 → 200, data updated"""
        sample_post["title"] = "Updated Title"
        res = client.put("/posts/1", sample_post)
        assert res.status_code == 200
        assert res.json()["title"] == "Updated Title"

    def test_delete_post(self, client):
        """DELETE /posts/1 → 200"""
        res = client.delete("/posts/1")
        assert res.status_code == 200

    def test_get_nonexistent_post(self, client):
        """GET /posts/9999 → 404"""
        res = client.get("/posts/9999")
        assert res.status_code == 404

    @pytest.mark.parametrize("post_id", [1, 5, 10, 50])
    def test_multiple_posts_exist(self, client, post_id):
        """Parametrized: check multiple post IDs"""
        res = client.get(f"/posts/{post_id}")
        assert res.status_code == 200
        assert res.json()["id"] == post_id

    def test_response_time(self, client):
        """Performance: response must be under 2 seconds"""
        res = client.get("/posts")
        assert res.elapsed.total_seconds() < 2.0

    def test_content_type_header(self, client):
        """Response header check"""
        res = client.get("/posts/1")
        assert "application/json" in res.headers["Content-Type"]
