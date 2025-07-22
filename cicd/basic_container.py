import dagger, asyncio

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
