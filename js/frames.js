/* Service pages: give boxes, buttons and photos the theme's crossed double border
   (the same h-lines / v-lines corners used on the "Book" buttons). */
(function () {
	function addLines(el) {
		el.insertAdjacentHTML("afterbegin", '<span class="h-lines"></span><span class="v-lines"></span>');
	}

	document.querySelectorAll(".svc-card, .svc-related a, .svc-header nav a.call").forEach(addLines);

	// Images can't hold the lines themselves, so each framed photo gets a wrapper
	document.querySelectorAll(".svc-split > img, .svc-hero.split img, .svc-gallery img").forEach(function (img) {
		var frame = document.createElement("span");
		frame.className = "photo-frame" + (img.classList.contains("fit") ? " fit" : "");
		img.parentNode.insertBefore(frame, img);
		frame.appendChild(img);
		addLines(frame);
	});
})();
