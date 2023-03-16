#!/usr/bin/env python3

import asyncio

task_tracker = []


def printgrid(grid):
    print("===========")
    for line in grid:
        print("".join(line))
    print("===========")


async def plant(grid, i, j):
    await asyncio.sleep(3)
    if grid[i][j] == "O":
        grid[i][j] = "."

        try:
            grid[i-1][j] = "."
            grid[i+1][j] = "."
            grid[i][j-1] = "."
            grid[i][j+1] = "."
        except IndexError:
            pass

    task_tracker.remove([i, j])


async def bomber_man(n, grid):
    newgrid = []
    for m in grid:
        newgrid.append(list(m))

    printgrid(newgrid)

    for TICK in range(n):
        if TICK == 0 or not (TICK % 2 == 0):
            for i in range(len(newgrid)):
                for j in range(len(newgrid[0])):
                    if newgrid[i][j] == "O":
                        if not [i, j] in task_tracker:
                            asyncio.create_task(plant(newgrid, i, j))
                            task_tracker.append([i, j])

        if TICK % 2 == 0:
            for i in range(len(newgrid)):
                for j in range(len(newgrid[0])):
                    if newgrid[i][j] == ".":
                        newgrid[i][j] = "O"

        printgrid(newgrid)
        await asyncio.sleep(1)

    last_grid = []
    for linee in newgrid:
        last_grid.append("".join(linee))

    return last_grid


async def main():
    how_many_seconds_str = input()
    if not how_many_seconds_str.isdigit():
        print("The first input must be an integer and must be the amount of seconds you want to enter")
        return
    n = int(how_many_seconds_str)

    grid = []

    first_line = input()
    grid.append(first_line)

    for _ in range(len(first_line) - 1):
        grid.append(input())

    print(await bomber_man(n, grid))


if __name__ == '__main__':
    asyncio.run(main())
