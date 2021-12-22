# BUILD : "release" | "debug" | "test"
BUILD = "release"

if BUILD == "test":
    DATABASE_NAME = "ACCS_TEST"
elif BUILD == "debug":
    DATABASE_NAME = "ACCS_DEBUG"
elif BUILD == "release":
    DATABASE_NAME = "ACCS_RELEASE"
#----------COMMON----------
DATABASE_CONNECTINO_STRING = f"mongodb://localhost:27017/{DATABASE_NAME}"
#------------------------------