from .helper import IntegrationHelper


class TestPhantom(IntegrationHelper):

    def test_create_container(self):
        """Test the ability of a Phantom instance to create one container."""
        cassette_name = self.cassette_name("create_container")
        with self.recorder.use_cassette(cassette_name):
            container = self.phantom.create_container({
                'name': 'test'
            })
        assert container['success']

    def test_containers(self):
        """Test the ability of a Phantom instance to get all containers."""
        cassette_name = self.cassette_name("containers")
        with self.recorder.use_cassette(cassette_name):
            containers = self.phantom.containers()
        assert len(containers) > 0

    def test_container(self):
        """Test the ability of a Phantom instance to get one container."""
        cassette_name = self.cassette_name("container")
        with self.recorder.use_cassette(self.cassette_name("containers")):
            containers = self.phantom.containers()
        with self.recorder.use_cassette(cassette_name):
            container = self.phantom.container(containers[0].id)
        assert container is not None

    def test_create_artifact(self):
        """Test the ability of a Phantom instance to create one artifact."""
        cassette_name = self.cassette_name("create_artifact")
        with self.recorder.use_cassette(self.cassette_name("containers")):
            containers = self.phantom.containers()
        with self.recorder.use_cassette(cassette_name):
            artifact = self.phantom.create_artifact({
                'container_id': containers[0].id,
                'source_data_identifier': self.source_data_identifier(10)
            })
        assert artifact['success']

    def test_artifacts(self):
        """Test the ability of a Phantom instance to get all artifacts."""
        cassette_name = self.cassette_name("artifacts")
        with self.recorder.use_cassette(cassette_name):
            artifacts = self.phantom.artifacts()
        assert len(artifacts) > 0

    def test_artifact(self):
        """Test the ability of a Phantom instance to get one artifact."""
        cassette_name = self.cassette_name("artifact")
        with self.recorder.use_cassette(self.cassette_name("artifacts")):
            artifacts = self.phantom.artifacts()
        with self.recorder.use_cassette(cassette_name):
            artifact = self.phantom.artifact(artifacts[0].id)
        assert artifact is not None

    def test_action_runs(self):
        """Test the ability of a Phantom instance to get all action runs"""
        cassette_name = self.cassette_name("action_runs")
        with self.recorder.use_cassette(cassette_name):
            action_runs = self.phantom.action_runs()
        assert len(action_runs) > 0

    def test_action_run(self):
        """Test the ability of a Phantom instance to get one action run"""
        cassette_name = self.cassette_name("action_run")
        with self.recorder.use_cassette(self.cassette_name("action_runs")):
            action_runs = self.phantom.action_runs()
        with self.recorder.use_cassette(cassette_name):
            action_run = self.phantom.action_run(action_runs[0].id)
        assert action_run is not None

    def test_assets(self):
        """Test the ability of a Phantom instance to get all assets"""
        cassette_name = self.cassette_name("assets")
        with self.recorder.use_cassette(cassette_name):
            assets = self.phantom.assets()
        assert len(assets) > 0

    def test_asset(self):
        """Test the ability of a Phantom instance to get one asset"""
        cassette_name = self.cassette_name("asset")
        with self.recorder.use_cassette(self.cassette_name("assets")):
            assets = self.phantom.assets()
        with self.recorder.use_cassette(cassette_name):
            asset = self.phantom.asset(assets[0].id)
        assert asset is not None

    def test_apps(self):
        """Test the ability of a Phantom instance to get all apps"""
        cassette_name = self.cassette_name("apps")
        with self.recorder.use_cassette(cassette_name):
            apps = self.phantom.apps()
        assert len(apps) > 0

    def test_app(self):
        """Test the ability of a Phantom instance to get one app"""
        cassette_name = self.cassette_name("app")
        with self.recorder.use_cassette(self.cassette_name("apps")):
            apps = self.phantom.apps()
        with self.recorder.use_cassette(cassette_name):
            app = self.phantom.app(apps[0].id)
        assert app is not None

    def test_version(self):
        """Test the ability of a Phantom instance to get the version."""
        cassette_name = self.cassette_name("version")
        with self.recorder.use_cassette(cassette_name):
            version = self.phantom.version()
        assert version['version'] is not None

    def test_system_info(self):
        """Test the ability of a Phantom instance to get the system information"""
        cassette_name = self.cassette_name("system_info")
        with self.recorder.use_cassette(cassette_name):
            system_info = self.phantom.system_info()
        assert system_info['base_url'] is not None
