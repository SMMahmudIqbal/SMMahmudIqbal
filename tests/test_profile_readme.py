import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ProfileSmokeTest(unittest.TestCase):
    def test_profile_readme_includes_banner_and_account_link(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.is_file())
        content = readme.read_text(encoding="utf-8")
        self.assertIn('src="banner.svg"', content)
        self.assertIn("https://github.com/SMMahmudIqbal", content)
if __name__ == "__main__": unittest.main()
