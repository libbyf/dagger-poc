import dagger, asyncio
from dagger import dag, function, object_type


# @object_type
# class Cicd:
#     @function
#     async def test(self, source: dagger.Directory) -> dagger.Directory:
#         """Tests the python application."""
#         print(f"Testing.......")
#         return (
#             dag.container()
#             .from_("python:3.12-slim")
#             .with_directory("/src", source.directory("python-app"))
#             .with_workdir("/src")
#             .with_exec(["pip", "install", "-r", "requirements.txt"])
#             .with_exec(["invoke test"])
#             .directory(".")
#         )

#     @function
#     async def build(self, source: dagger.Directory) -> dagger.File:
#         """Builds the python application."""

#         tested_src = await self.test(source)

#         return (
#             dag.container()
#             .from_("python:3.12-slim")
#             .with_directory("/src", tested_src)
#             .with_workdir("/src")
#             .with_exec(["pip", "install", "-r", "requirements.txt"])
#             .with_entrypoint(["python", "main.py"])
#             .as_tarball()
#         )

# async def main():
#     async with dagger.Connection() as client:
#         # assumes your code is in ./cicd/python-app/
#         source_dir = client.host().directory(".", exclude=[".venv", "__pycache__"])
#         result = await Cicd().test(source_dir)
#         print("✅ Test completed")

# asyncio.run(main())

async def main():
    print("Starting Dagger CI/CD example...")
    async with dagger.Connection() as client:
        out = await (
            client.container()
            .from_("alpine")
            .with_exec(["echo", "Hello from Dagger!"])
            .stdout()
        )

        print(f"✅ Output: {out}")
    print("Done Dagger CI/CD example...")

asyncio.run(main())
