build:
	docker build -t teeny .

run:
	docker run -it -p5000:5000 teeny bash
