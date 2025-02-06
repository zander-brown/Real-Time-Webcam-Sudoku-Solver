print('Importing code and libraries from other files...')

from webcam_sudoku_solver import *
import pyautogui

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # hide tf warnings
import tensorflow as tf


def main():
	model = tf.keras.models.load_model('models/handwritten_cnn.h5')

	# create the core of the program
	webcam_sudoku_solver = WebcamSudokuSolver(model)

	print('Logs:')
	while True:
		# capture screenshot
		screenshot = pyautogui.screenshot()
		frame = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

		# run the core of the program
		output_frame = webcam_sudoku_solver.solve(frame)

		# output results
		cv.imshow('Screen Sudoku Solver', output_frame)

		# check if a user has pressed a key, if so, close the program
		if cv.waitKey(1) >= 0:
			break

	cv.destroyAllWindows()


if __name__ == "__main__":
	main()

print('Code is done, so everything works fine!')
