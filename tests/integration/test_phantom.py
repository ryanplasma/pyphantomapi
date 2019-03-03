from .helper import IntegrationHelper


class TestPhantom(IntegrationHelper):
    def test_containers(self):
        """Test the ability of a GitHub instance to get all artifacts."""
        cassette_name = self.cassette_name("containers")
        with self.recorder.use_cassette(cassette_name):
            containers = self.phantom.containers()
        assert len(containers) > 0

    def test_container(self):
        """Test the ability of a GitHub instance to get one artifact."""
        cassette_name = self.cassette_name("container")
        with self.recorder.use_cassette(cassette_name):
            container = self.phantom.container(1)
        assert container is not None

    def test_create_container(self):
        """Test the ability of a GitHub instance to get one artifact."""
        cassette_name = self.cassette_name("create_container")
        with self.recorder.use_cassette(cassette_name):
            container = self.phantom.create_container({
                'name': 'test'
            })
        assert container['success']

    def test_artifacts(self):
        """Test the ability of a GitHub instance to get all artifacts."""
        cassette_name = self.cassette_name("artifacts")
        with self.recorder.use_cassette(cassette_name):
            artifacts = self.phantom.artifacts()
        assert len(artifacts) > 0

    def test_artifact(self):
        """Test the ability of a GitHub instance to get one artifact."""
        cassette_name = self.cassette_name("artifact")
        with self.recorder.use_cassette(cassette_name):
            artifact = self.phantom.artifact(1)
        assert artifact is not None

    def test_create_artifact(self):
        """Test the ability of a GitHub instance to get one artifact."""
        cassette_name = self.cassette_name("create_artifact")
        with self.recorder.use_cassette(cassette_name):
            artifact = self.phantom.create_artifact({
                'container_id': 1
            })
        assert artifact['success']

    def test_version(self):
        """Test the ability of a Phantom instance to get the version."""
        cassette_name = self.cassette_name("version")
        with self.recorder.use_cassette(cassette_name):
            version = self.phantom.version()
        assert version['version'] is not None
