from setuptools import setup, find_packages

setup(
    name="rticonnector",
    version="1.0.9",
    packages=find_packages(include=["rticonnector", "rticonnector.*"]),
    package_data={
        "rticonnector": ["Configuration/BarakQosProfile.xml"],
    },
    install_requires=[
        "colorama",
        "loguru",
        "rti.connext",
        "win32-setctime"
    ],
    python_requires='>=3.9'
)
