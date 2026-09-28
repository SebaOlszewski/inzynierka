import unittest
from cube_bitboard import BitCube
from blind_bit import (
    BlindUnsupportedState,
    CORNER_SWAP_ALGORITHM,
    EDGE_SWAP_ALGORITHM,
    apply_algorithm,
    _inverse_algorithm,
    solve_blind,
    solved_bit_state,
    validate_bitcube_moves,
)


class BlindSolverTests(unittest.TestCase):
    def test_solved_cube_needs_no_moves(self):
        cube = BitCube()
        log = []

        solve_blind(cube, log)

        self.assertEqual(log, [])
        self.assertTrue(solved_bit_state(cube))

    def test_verified_edge_commutator_is_executed_without_search(self):
        cube = BitCube()
        for move in _inverse_algorithm(EDGE_SWAP_ALGORITHM).split():
            cube.apply_move(move)
        log = []

        solve_blind(cube, log)

        self.assertEqual(validate_bitcube_moves(log), [])
        self.assertTrue(solved_bit_state(cube))
        self.assertEqual(cube.edges, BitCube().edges)
        self.assertEqual(cube.corners, BitCube().corners)

    def test_verified_corner_commutator_is_executed_without_search(self):
        cube = BitCube()
        for move in _inverse_algorithm(CORNER_SWAP_ALGORITHM).split():
            cube.apply_move(move)
        log = []

        solve_blind(cube, log)

        self.assertEqual(validate_bitcube_moves(log), [])
        self.assertTrue(solved_bit_state(cube))

    def test_unsupported_commutator_is_explicit_and_does_not_mutate(self):
        cube = BitCube()
        cube.apply_move("R")
        before = (cube.edges, cube.corners)

        with self.assertRaises(BlindUnsupportedState):
            solve_blind(cube, [])

        self.assertEqual((cube.edges, cube.corners), before)

    def test_supplied_swap_algorithms_are_legal(self):
        self.assertEqual(validate_bitcube_moves(EDGE_SWAP_ALGORITHM), [])
        self.assertEqual(validate_bitcube_moves(CORNER_SWAP_ALGORITHM), [])

    def test_supplied_swap_algorithms_have_legal_inverse_round_trip(self):
        def inverse(algorithm):
            moves = algorithm.split()
            return tuple(
                move if move.endswith("2") else
                move[:-1] if move.endswith("'") else move + "'"
                for move in reversed(moves)
            )

        for algorithm in (EDGE_SWAP_ALGORITHM, CORNER_SWAP_ALGORITHM):
            cube = BitCube()
            apply_algorithm(cube, algorithm)
            apply_algorithm(cube, " ".join(inverse(algorithm)))
            self.assertTrue(solved_bit_state(cube))


if __name__ == "__main__":
    unittest.main()
