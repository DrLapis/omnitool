# (left, right, up, down)
none = [(1 * 18, 1 * 18), (2 * 18, 1 * 18), (3 * 18, 1 * 18)]
fail = [(2, 0, 1, 2), (2, 1, 2, 0), (0, 2, 2, 0), (0, 2, 2, 2),
        (0, 2, 0, 2), (1, 0, 2, 0), (0, 1, 0, 2), (1, 0, 0, 2),
        (0, 1, 2, 2), (0, 1, 2, 0), (0, 2, 2, 1), (2, 0, 2, 2),
        (0, 2, 1, 2), (0, 2, 0, 1), (1, 2, 2, 0), (0, 2, 1, 0),
        (2, 2, 0, 2), (2, 1, 0, 2), (2, 0, 1, 0), (2, 0, 0, 1),
        (1, 0, 2, 2), (1, 2, 0, 2), (2, 0, 2, 1), (2, 2, 0, 1),
        (2, 0, 0, 2), (2, 2, 2, 0), (2, 0, 2, 0), (2, 2, 1, 0)]
mix_detail = {
    (2, 1, 2, 1): [(2 * 18, 5 * 18), (2 * 18, 7 * 18), (2 * 18, 9 * 18)],
    (1, 2, 2, 1): [(3 * 18, 5 * 18), (3 * 18, 7 * 18), (3 * 18, 9 * 18)],
    (2, 1, 1, 2): [(2 * 18, 6 * 18), (2 * 18, 8 * 18), (2 * 18, 10 * 18)],
    (1, 2, 1, 2): [(3 * 18, 6 * 18), (3 * 18, 8 * 18), (3 * 18, 10 * 18)],
    (0, 1, 1, 2): [(4 * 18, 5 * 18), (4 * 18, 6 * 18), (4 * 18, 7 * 18)],
    (1, 0, 1, 2): [(5 * 18, 5 * 18), (5 * 18, 6 * 18), (5 * 18, 7 * 18)],
    (0, 1, 2, 1): [(4 * 18, 8 * 18), (4 * 18, 9 * 18), (4 * 18, 10 * 18)],
    (1, 0, 2, 1): [(5 * 18, 8 * 18), (5 * 18, 9 * 18), (5 * 18, 10 * 18)],
    (0, 0, 0, 2): [(6 * 18, 5 * 18), (6 * 18, 6 * 18), (6 * 18, 7 * 18)],
    (0, 0, 2, 0): [(6 * 18, 8 * 18), (6 * 18, 9 * 18), (6 * 18, 10 * 18)],
    (0, 0, 1, 2): [(7 * 18, 5 * 18), (7 * 18, 6 * 18), (7 * 18, 7 * 18)],
    (0, 0, 2, 1): [(7 * 18, 8 * 18), (7 * 18, 9 * 18), (7 * 18, 10 * 18)],
    (1, 1, 2, 1): [(8 * 18, 6 * 18), (9 * 18, 6 * 18), (10 * 18, 6 * 18)],
    (1, 2, 1, 1): [(8 * 18, 7 * 18), (8 * 18, 8 * 18), (8 * 18, 9 * 18)],
    (1, 1, 1, 2): [(8 * 18, 5 * 18), (9 * 18, 5 * 18), (10 * 18, 5 * 18)],
    (2, 1, 1, 1): [(9 * 18, 7 * 18), (9 * 18, 8 * 18), (9 * 18, 9 * 18)],
    (2, 2, 1, 1): [(10 * 18, 7 * 18), (10 * 18, 8 * 18), (10 * 18, 9 * 18)],
    (1, 1, 2, 2): [(8 * 18, 10 * 18), (9 * 18, 10 * 18), (10 * 18, 10 * 18)],
    (2, 2, 2, 1): [(11 * 18, 5 * 18), (11 * 18, 6 * 18), (11 * 18, 7 * 18)],
    (2, 1, 2, 2): [(12 * 18, 5 * 18), (12 * 18, 6 * 18), (12 * 18, 7 * 18)],
    (2, 2, 1, 2): [(11 * 18, 8 * 18), (11 * 18, 9 * 18), (11 * 18, 10 * 18)],
    (1, 2, 2, 2): [(12 * 18, 8 * 18), (12 * 18, 9 * 18), (12 * 18, 10 * 18)],
    (1, 1, 0, 2): [(13 * 18, 0), (14 * 18, 0), (15 * 18, 0)],
    (1, 1, 2, 0): [(13 * 18, 18), (14 * 18, 18), (15 * 18, 18)],
    (0, 2, 1, 1): [(13 * 18, 2 * 18), (14 * 18, 2 * 18), (15 * 18, 2 * 18)],
    (2, 0, 1, 1): [(13 * 18, 3 * 18), (14 * 18, 3 * 18), (15 * 18, 3 * 18)],
    #lower 4
    (2, 1, 0, 1): [(0, 11 * 18), (18, 11 * 18), (2 * 18, 11 * 18)],
    (1, 2, 0, 1): [(3 * 18, 11 * 18), (4 * 18, 11 * 18), (5 * 18, 11 * 18)],
    (2, 2, 2, 2): [(6 * 18, 11 * 18), (7 * 18, 11 * 18), (8 * 18, 11 * 18)],
    (2, 2, 0, 0): [(9 * 18, 11 * 18), (10 * 18, 11 * 18), (11 * 18, 11 * 18)],
    #lower 3
    (2, 1, 1, 0): [(0, 12 * 18), (18, 12 * 18), (2 * 18, 12 * 18)],
    (1, 2, 1, 0): [(3 * 18, 12 * 18), (4 * 18, 12 * 18), (5 * 18, 12 * 18)],
    (0, 0, 2, 2): [(6 * 18, 12 * 18), (6 * 18, 13 * 18), (6 * 18, 14 * 18)],
    #lower 2
    (2, 0, 0, 0): [(0, 13 * 18), (18, 13 * 18), (2 * 18, 13 * 18)],
    (0, 2, 0, 0): [(3 * 18, 13 * 18), (4 * 18, 13 * 18), (5 * 18, 13 * 18)],
    #lowest
    (2, 1, 0, 0): [(0, 14 * 18), (18, 14 * 18), (2 * 18, 14 * 18)],
    (1, 2, 0, 0): [(3 * 18, 14 * 18), (4 * 18, 14 * 18), (5 * 18, 14 * 18)],
}

##grass_detail = {
##    #upper 3
##    (0,2,1,1) : [(0*18, 0*18),(0*18, 1*18),(0*18, 2*18)],
##    (1,1,0,2) : [(1*18, 0*18),(2*18, 0*18),(3*18, 0*18)],
##    (2,2,2,2) : [(1*18, 1*18),(2*18, 1*18),(3*18, 1*18)],
##    (1,1,2,0) : [(1*18, 2*18),(2*18, 2*18),(3*18, 2*18)],
##    (2,0,1,1) : [(4*18, 0*18),(4*18, 1*18),(4*18, 2*18)],
##    (0,0,1,1) : [(5*18, 0*18),(5*18, 1*18),(5*18, 2*18)],
##    (0,0,0,1) : [(6*18, 0*18),(7*18, 0*18),(8*18, 0*18)],
##    (0,0,0,1) : [(6*18, 0*18),(7*18, 0*18),(8*18, 0*18)],
from blend import mix

for key in fail:
    mix_detail[key] = none
for key in mix:
    mix_detail[key] = mix[key]

override = {
    (1, 1, 0, 2): [(1 * 18, 0 * 18), (2 * 18, 0 * 18), (3 * 18, 0 * 18)],
    (0, 2, 1, 1): [(0, 0), (0, 18), (0, 2 * 18)],
    (1, 1, 2, 0): [(18, 2 * 18), (18 * 2, 2 * 18), (18 * 3, 2 * 18)],
    (2, 0, 1, 1): [(72, 0), (72, 18), (72, 18 * 2)],

}
grass_detail = {}
for key in mix_detail:
    if key in override:
        grass_detail[key] = override[key]
    else:
        grass_detail[key] = mix_detail[key]