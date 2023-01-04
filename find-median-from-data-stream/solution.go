type Heap struct {
	s []int
}

func (h *Heap) Pop() int {
	res := h.s[0]
	h.s[0] = h.s[len(h.s)-1]
	h.s = h.s[:len(h.s)-1]
	h.sift_down(0)
	return res
}

func (h *Heap) Push(el int) {
	h.s = append(h.s, el)
	h.sift_up(len(h.s) - 1)
}

func (h *Heap) sift_up(i int) {
	for {
		if i == 0 {
			return
		}
		r := (i - 1) / 2
		if h.s[i] <= h.s[r] {
			return
		}
		h.s[i], h.s[r] = h.s[r], h.s[i]
		i = r
	}
}

func (h *Heap) sift_down(i int) {
	for {
		l, r := i*2 + 1, (i + 1) * 2
		if len(h.s) == l+1 {
			if h.s[i] < h.s[l] {
				h.s[i], h.s[l] = h.s[l], h.s[i]
			}
			return
		}
		if len(h.s) <= l {
			return
		}
		a := 0
		if h.s[l] <= h.s[r] {
			a = r
		} else {
			a = l
		}
		if h.s[a] <= h.s[i] {
			return
		}
		h.s[i], h.s[a] = h.s[a], h.s[i]
		i = a
	}
}


type MedianFinder struct {
	l Heap
	r Heap
}

func Constructor() MedianFinder {
	return MedianFinder{
		l: Heap{},
		r: Heap{},
	}
}

func (this *MedianFinder) AddNum(num int) {
	if len(this.l.s) == 0 {
		this.l.Push(num)
		return
	}
	if float64(num) <= this.FindMedian() {
		this.l.Push(num)
	} else {
		this.r.Push(-num)
	}

	for len(this.l.s)+1 < len(this.r.s) {
		this.l.Push(-this.r.Pop())
	}
	for len(this.r.s)+1 < len(this.l.s) {
		this.r.Push(-this.l.Pop())
	}
}

func (this *MedianFinder) FindMedian() float64 {
	if len(this.l.s) == len(this.r.s) {
		return float64(this.l.s[0]-this.r.s[0]) / 2
	} else if len(this.l.s) < len(this.r.s) {
		return float64(-this.r.s[0])
	}
	return float64(this.l.s[0])
}



/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */