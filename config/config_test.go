package config

import (
	"testing"
)

func TestByInvitationalPath(t *testing.T) {
	Conf()
	if ByInvitationalPath("b") != "/run/media/karmanyaahm/scioly/oldstff/tests/organized_by_invitational-b" {
		t.Fail()
	}
	if ByInvitationalPath("B") != "/run/media/karmanyaahm/scioly/oldstff/tests/organized_by_invitational-b" {
		t.Fail()
	}
}
