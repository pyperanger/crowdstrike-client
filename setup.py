import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CrowdStrike Client API",
    version="0.0.1",
    author="Pyperanger",
    description="A Non-oficial crowdstrike client api",
    url="https://github.com/pyperanger/crowdstrike-client",
    project_urls={
        "Bug Tracker": "https://github.com/pyperanger/crowdstrike-client/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)