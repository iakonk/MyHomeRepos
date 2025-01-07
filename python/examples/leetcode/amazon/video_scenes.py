	01234567890123456780
film	ababcbacadefegdehijhklij
a	s       e
b	 s   e
c        s  e
d             s    e
e              s    e
f               u
g

Constraints:
n = len(film)
{'a': (0, 8), 'b': (1, 5), 'c': (3, 5), 'd'}
TC: O(n), MC: O(n)
1. Seq scan: [s, e], [s, e]
2. Merge intervals
	1. init open_int = 0
	2. inc open_int when a int starts
	3. dec open_int when a int ends
	4. when open_int == 0 we know the len of the scene

def cutFilms(shots: list[str]) -> list[int]:
  if not shots:
    return []
  events = {}
  for ix, shot in enumerate(shots):
    if shot is shots:
      events[shot] = [ix, ix]
    else:
      events[shot][1] = ix
  scene_lengths = []
  open_intervals = 0
  scene_start = -1
  for ix, shot in enumerate(shots):
     if ix not in events[shot]:
       continue
     s, e = events[shot]
     if ix == s:
       open_intervals += 1
     if ix == e:
       open_intervals -= 1
       if open_intervals == 0:
         scene_lengths.append(e - scene_start)
       scene_start = e
  return scene_lengths
