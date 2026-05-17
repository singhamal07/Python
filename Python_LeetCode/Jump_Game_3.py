class Solution:
      def canReach(self, arr: list[int], start: int) -> bool:
          n = len(arr)
          visited = set()
          queue = [start]
          while queue:
              i = queue.pop()
              if arr[i] == 0:
                  return True
              if i in visited:
                  continue
              visited.add(i)
              for ni in (i + arr[i], i - arr[i]):
                  if 0 <= ni < n and ni not in visited:
                      queue.append(ni)
          return False
